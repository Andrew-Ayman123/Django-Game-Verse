import json
from channels.generic.websocket import WebsocketConsumer


class WordleConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        guessed_word = text_data_json['guessedWord'].lower()
        sent_data={}
        if self.scope['session']['wordle-attrs']:
            original_word = self.scope['session']['wordle-attrs']['word']
            guesses = self.scope['session']['wordle-attrs']['guesses']

            if len(guessed_word) != 5 or guesses <= 0:
                return
            guesses -= 1

            self.scope['session']['wordle-attrs']['guesses'] = guesses
            self.scope['session'].save()
            correct_letters = {
                index for index,(letter, correct) in enumerate(zip(guessed_word, original_word)) if letter == correct
            }
            misplaced_letters = set(guessed_word) & set(original_word)

            guessed_output = [
                'c' if index in correct_letters else 'm' if letter in misplaced_letters else 'w' for index,letter in enumerate(guessed_word)]
            success=all((letter =='c' for letter in guessed_output))
            if success:
                self.scope['session']['wordle-attrs']['success-from-consumer']=True
                self.scope['session'].save()
            sent_data['guessedOutput']=guessed_output
            sent_data['guesses']=guesses
            
        else:
            sent_data['refresh']=True

        self.send(text_data=json.dumps(sent_data))
