from django.urls import path
from . import views

urlpatterns=[
  path("",views.home,name="home"),
  path("math",views.math_game,name="math"),
  path("tic_tac_toe",views.tic_game,name="tic_tac_toe"),
  path("snake",views.snake_game,name="snake")
]