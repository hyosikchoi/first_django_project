from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from polls.models import Question


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def results(request, question_id):
    response = "You're voting on question %s." % question_id
    return HttpResponse(response)

def details(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)