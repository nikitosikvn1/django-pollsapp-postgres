from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice

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
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choices.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "pollsapp/detail.html", {
            "question": question,
            "error_message": "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('pollsapp:result', args=(question.id,)))


def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "pollsapp/result.html", {
        "question": question
    })
