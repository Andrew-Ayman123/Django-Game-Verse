from django.db import models

# Create your models here.

class LeaderBoard(models.Model):
  name=models.CharField(max_length=20,primary_key=True)

  def __str__(self) -> str:
    return self.name
  

class LeaderBoardItem(models.Model):
  leaderboard = models.ForeignKey(LeaderBoard, on_delete=models.CASCADE)
  name=models.CharField(max_length=50)
  date=models.DateTimeField()
  score=models.IntegerField()

  def __str__(self) -> str:
    return f'{self.name} {self.date} {self.score}'
