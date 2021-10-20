import datetime

from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    return HttpResponse("Hello, World!!!")


def date_view(request):
    date = datetime.datetime.now()
    return HttpResponse(f"Now is {date}")
