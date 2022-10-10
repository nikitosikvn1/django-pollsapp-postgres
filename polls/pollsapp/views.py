from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("This is main page")

def detail(request, question_id):
    return HttpResponse("Question details will be displayed here #%s" % question_id)

def vote(request, question_id):
    return HttpResponse("You can vote on this page #%s" % question_id)

def result(request, question_id):
    return HttpResponse("Poll results will be displayed here #%s" % question_id)