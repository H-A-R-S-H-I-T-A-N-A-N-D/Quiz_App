from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Question, Quiz

import json


def index(request):
    return HttpResponse("Welcome!")


@csrf_exempt
def question(request):
    if request.method == "POST":
        req = json.loads(request.body.decode('utf-8'))
        questionid = req["questionid"]
        question = req["question"]
        optiona = req["optiona"]
        optionb = req["optionb"]
        optionc = req["optionc"]
        optiond = req["optiond"]
        answer = req["answer"]
        # options = {"optiona": optiona, "optionb": optionb, "optionc": optionc, "optiond": optiond}
        # question = Question(question, options, answer)
        question = Question(questionid, question, optiona, optionb, optionc, optiond, answer)
        question.save()
        return HttpResponse("Created question")
    elif request.method == "GET":
        data = list(Question.objects.values())
        return JsonResponse(data, safe=False)
    else:
        return HttpResponse("Invalid Request")


@csrf_exempt
def quiz(request):
    if request.method == "POST":
        req = json.loads(request.body.decode('utf-8'))
        quizid = req["quizid"]
        countofque = req["countofque"]
        questions = req["questions"]
        quiz = Quiz(quizid, countofque)
        quiz.save()
        quiz = Quiz.objects.get(quizid=quizid)
        for questionid in questions:
            print(questionid, type(questionid))
            question = Question.objects.get(questionid=questionid)
            print(question, type(question))
            # quiz.questions.add(question)
            question.quiz_set.add(quiz)
            question.save()
            quiz.save()
        return HttpResponse("Created quiz")
    elif request.method == "GET":
        a = Quiz.objects.values()
        print(a)
        data = list(a)
        print(data)
        return JsonResponse(data, safe=False)
    else:
        return HttpResponse("Invalid Request")
    # return JsonResponse(response, safe=False)


@csrf_exempt
def questionbyid(request, questionid):
    if request.method == "GET":
        data = list(Question.objects.filter(questionid=questionid).values())
        return JsonResponse(data, safe=False)
    elif request.method == "DELETE":
        data = Question.objects.filter(questionid=questionid)
        if data.exists():
            data.delete()
            response = HttpResponse("Deleted", 200)
        else:
            response = HttpResponse(status=204)
        return response

