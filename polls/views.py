from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import HttpResponse, render
from .models import Question, Choice

# Create your views here.

def index(request):
    q = Question.objects.order_by('-pub_date')
    return render(request, 'polls/index.html',
    {
       "question_list": q 
    }
    )


def say_name(request, name):
    return render(request, "polls/index.html",
        {
            "name": name
        }
    )


def details(request, question_id):
    q = Question.objects.filter(pk=question_id)
    print(q[0].question)

    return render(request, "polls/details.html",
    {
        "ques": q[0]
    })

def vote(request, question_id):
    question = Question.objects.get(pk=question_id)
    try:
        print(request.POST['choice'])
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError):
        return render(request, "polls/details.html", 
        {
            "ques": question,
            "error_message": "You didn't selected any option"
        }
        )
    selected_choice.votes+=1
    selected_choice.save()
    return HttpResponseRedirect(reverse('result', args=(question.id,)))


def result(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(request, "polls/results.html", 
        {
           "question": question 
        }
    )



    


