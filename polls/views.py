from django.http import HttpResponse
from django.shortcuts import HttpResponse, render
from .models import Question, Choice

# Create your views here.

def index(request):
    q = Question.objects.order_by('-pub_date')[:3]
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

#def vote(request, question_id):
    


