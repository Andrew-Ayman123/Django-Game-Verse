from django.urls import path
from . import views

urlpatterns=[
  path("",views.home,name="home"),
  path("math",views.math_game,name="math"),
  path("wordle",views.wordle_game,name="wordle"),
]