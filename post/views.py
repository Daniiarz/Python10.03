import datetime
import random
from typing import List

from django.conf import settings
from django.http import HttpResponse, FileResponse, HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import BlogPost, Comment


def hello_world(request):
    return HttpResponse("Hello, World!!!")


def date_view(request):
    date = datetime.datetime.now()
    return HttpResponse(f"Now is {date}")


def create_blog_view(request):
    if request.method == "POST":
        data = request.POST
        files = request.FILES
        title = data.get("title")
        description = data.get("description")
        image = files.get("image")
        BlogPost.objects.create(title=title, image=image, description=description)
        return redirect("post-list")
    elif request.method == "GET":
        return render(request, "blog_create.html")


def file_response(request):
    file = open(f"{settings.BASE_DIR}/post/123.jpg", "rb")
    return FileResponse(file)


def random_fruit_number():
    num: int = random.randint(1, 1000)
    fruit: str = random.choice(["apple", "mango", "watermelon", "banana", "orange"])
    return num, fruit


class PostListView(ListView):
    template_name = "index.html"
    queryset: List[BlogPost] = BlogPost.objects.all()
    context_object_name = "blogs"

    def get_context_data(self, *, object_list=None, **kwargs):
        context: dict = super(PostListView, self).get_context_data(object_list=None, **kwargs)
        num, fruit = random_fruit_number()
        context["num"] = num
        context["fruitzz"] = fruit
        return context


class PostDetailView(DetailView):
    queryset = BlogPost.objects.all()
    template_name = "blog_detail.html"
    context_object_name = "blog"

    def get_context_data(self, **kwargs):
        context: dict = super(PostDetailView, self).get_context_data(**kwargs)
        pk = self.kwargs["pk"]
        comments: List[Comment] = Comment.objects.filter(post_id=pk)
        context["comments"] = comments
        return context


def create_comment_view(request: HttpRequest, post_id: int):
    if request.method == "POST":
        data: dict = request.POST
        if data.get("text"):
            Comment.objects.create(text=data["text"], post_id=post_id)
            return HttpResponse("Comment added!")
        else:
            return HttpResponse("NETU TEXTA!")
