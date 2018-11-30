from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Question, Choice
from django.urls import reverse
from django.views import generic


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {
#         "latest_question_list" : latest_question_list,
#     }
#     return render(request, "polls/index.html", context)
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": question})
class DetailView(generic.DetailView):
    template_name = 'polls/detail.html'
    model = Question


# def results(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#   return render(request, 'polls/results.html', {'question': question})
class ResultsView(generic.DetailView):
    template_name = 'polls/results.html'
    model = Question


def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        select_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        select_choice.votes += 1
        select_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
