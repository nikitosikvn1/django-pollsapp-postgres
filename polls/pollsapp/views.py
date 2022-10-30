from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Sum, Q
from .models import Question, Choice

# Create your views here.

def index(request):
    search_query = request.GET.get("search")
    
    if search_query:
        latest_question_list = Question.objects.filter(Q(question__icontains=search_query) | Q(date__icontains=search_query))
        header = f"Search results for: '{search_query}'"
    else:
        latest_question_list = Question.objects.order_by('-date')[:5]
        header = "Recent questions"

    votes_num = [num.choices.aggregate(Sum('votes'))['votes__sum'] for num in latest_question_list]

    questions_votes = zip(latest_question_list, votes_num)
    return render(request, "pollsapp/index.html", {
        "questions_votes": questions_votes,
        "header": header
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

    data = {
        "labels": [choice.choice for choice in question.choices.all()],
        "values": [vote.votes for vote in question.choices.all()]
    }

    return render(request, "pollsapp/result.html", {
        "question": question,
        "data": data
    })