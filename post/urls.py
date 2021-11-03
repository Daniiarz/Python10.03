from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostListView.as_view()),
    path("<int:pk>/", views.PostDetailView.as_view()),
    path("comment/<int:post_id>/", views.create_comment_view),
    path("date/", views.date_view),
    path("file/", views.file_response),
]
