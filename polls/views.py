from django.http import HttpResponse
from django.shortcuts import render_to_response,get_object_or_404
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        "latest_question_list" : latest_question_list,
    }
    return render_to_response("polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render_to_response("polls/detail.html", {"question": question})


def results(request, question_id):
    return HttpResponse("You are looking at the ansult of question %s" % question_id)


def vote(request,question_id):
    return HttpResponse("You are voting on question %s" % question_id)

