from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question', views.question, name='question'),
    path('question/<str:questionid>', views.questionbyid, name='questionbyid'),
    path('quiz', views.quiz, name='quiz'),

]
