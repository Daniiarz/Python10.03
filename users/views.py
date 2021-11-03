# Create your views here.
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render

from users.forms import RegistrationForm
from users.models import CustomUser


def register_view(request):
    if request.method == "POST":
        data: dict = request.POST
        form = RegistrationForm(data=data)
        if form.is_valid():
            valid_data = form.cleaned_data
            CustomUser.objects.create_user(
                username=valid_data["username"],
                email=valid_data["email"],
                password=valid_data["password"],
                first_name=valid_data["first_name"],
                last_name=valid_data["last_name"],
            )
            return HttpResponse("Пользователь был создан успешно")
        else:
            return render(request, "register_form.html", context={"form": form})
    if request.method == "GET":
        return render(request, "register_form.html", context={"form": RegistrationForm()})


def login_view(request):
    if request.method == "POST":
        data: dict = request.POST
        if not data.get("username"):
            return HttpResponse("Имя пользователя не указано")
        if not data.get("password"):
            return HttpResponse("Нету пароля")
        user = authenticate(
            request,
            username=data["username"],
            password=data["password"],
        )
        if user is not None:
            login(request, user)
            return HttpResponse("Успешный логин")
        else:
            return HttpResponse("Не верное имя пользователя или пароль")

    if request.method == "GET":
        return render(request, "login_form.html")


def logout_view(request):
    logout(request)

    return HttpResponse("Вы вышли")
