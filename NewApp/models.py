from django.db import models


# Create your models here.
class Question(models.Model):
    questionid = models.AutoField(primary_key=True)
    question = models.TextField()
    optiona = models.TextField()
    optionb = models.TextField()
    optionc = models.TextField()
    optiond = models.TextField()
    answer = models.TextField()


class Quiz(models.Model):
    quizid = models.AutoField(primary_key=True)
    countofque = models.IntegerField()
    questions = models.ManyToManyField(Question)

"""
Quiz - 
quizid
no of questions
list of que[]


Submissions - 
Quiz
list of answer 
score

Question - 
question
list of ans possible, 
actual answer



"""
