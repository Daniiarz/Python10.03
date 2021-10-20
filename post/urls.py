from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_view),
    path("date/", views.date_view),
    path("file/", views.file_response),
]
