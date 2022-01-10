from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, response
from .models import Question, Choice
from django.template import loader
from django.http import Http404
from django.urls import reverse
# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except:
        raise Http404("Question does not exist.")
    return render(request, 'polls/detail.html', {
        'question': question
    })
# A Shortcut :get_object_or_404()


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            "question": question,
            "error_message": "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return response.HttpResponseRedirect(reverse('polls:result', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/resu;ts.html',{
        "question":question
    })


