import datetime
import random
from typing import List

from django.http import HttpResponse, FileResponse, HttpRequest
from django.conf import settings
from django.shortcuts import render

from .models import BlogPost


def hello_world(request):
    return HttpResponse("Hello, World!!!")


def date_view(request):
    date = datetime.datetime.now()
    return HttpResponse(f"Now is {date}")


def file_response(request):
    file = open(f"{settings.BASE_DIR}/post/123.jpg", "rb")
    return FileResponse(file)


def blog_view(request: HttpRequest):
    num: int = random.randint(1, 1000)
    fruit: str = random.choice(["apple", "mango", "watermelon", "banana"])
    blogs: List[BlogPost] = BlogPost.objects.all()
    return render(request, "index.html", context={"num": num, "fruitzz": fruit, "blogs": blogs})
