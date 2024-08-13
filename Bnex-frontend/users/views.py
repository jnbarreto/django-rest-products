from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
import requests

HEADER = {"Authorization": "Token b1bb35a1ce4c76b8d23cef79b02958d2d1a555ee"}

def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name= request.POST.get("last_name")
        email = request.POST.get("email")
        cpf = request.POST.get("cpf")
        password = request.POST.get("password")
        confirmar_password = request.POST.get("confirm_password")
        user = {
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "cpf": cpf,
            "password": password,
            "confirm_password": confirmar_password,
        }

        response = requests.post(url="http://localhost:8080/api/v1/auth/registration/", headers=HEADER, data=user)
        if response.status_code == 201:
            return redirect('/users/auth/sign-in')

        messages.add_message(request,constants.ERROR, f"{response.json()}")
        return redirect('/users/register')


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        response = requests.post(url="http://localhost:8080/api/v1/auth/sign-in/", headers=HEADER, data={"username": username, "password": password})
        if response.status_code == 200:
            return redirect('/products/list')

        messages.add_message(request,constants.ERROR, "Usuário ou senha inválidos.")
        return redirect('/users/auth/sign-in')