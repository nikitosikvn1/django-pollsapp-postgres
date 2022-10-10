from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-date')[:5]

    return render(request, "pollsapp/index.html", {
        "latest_question_list": latest_question_list
    })


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "pollsapp/detail.html", {
        "question": question
    })


def vote(request, question_id):
    return HttpResponse("You can vote on this page #%s" % question_id)


def result(request, question_id):
    return HttpResponse("Poll results will be displayed here #%s" % question_id)