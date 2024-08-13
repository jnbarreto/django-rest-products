from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
import requests

HEADER = {"Authorization": "Token b1bb35a1ce4c76b8d23cef79b02958d2d1a555ee"}

def list(request):
    if request.method == "GET":
        response = requests.get(url="http://localhost:8080/api/v1/products/", headers=HEADER)
        if response.status_code == 200:
            print('lissssst', response.json()['results'])
            return render(request, "list.html", {'products':response.json()['results']})


def detail(request, **kwargs):
    if request.method == "GET":
        id = kwargs.get('pk')
        response = requests.get(url=f"http://localhost:8080/api/v1/products/{id}/", headers=HEADER)
        if response.status_code == 200:
            return render(request, "detail.html", {'product':response.json()})


def create(request):
    if request.method == "GET":
        return render(request, "new.html")
    elif request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        value= request.POST.get("value")
        product = {
            "name": name,
            "description": description,
            "value": value,
        }

        response = requests.post(url="http://localhost:8080/api/v1/products/", headers=HEADER, data=product)
        if response.status_code == 201:
            return redirect('/products/list')

        messages.add_message(request,constants.ERROR, f"{response.json()}")
        return redirect('/products/create')


def update(request, **kwargs):
    id = kwargs.get('pk')
    if request.method == "GET":
        response = requests.get(url=f"http://localhost:8080/api/v1/products/{id}/", headers=HEADER)
        if response.status_code == 200:
            return render(request, "update.html", {'product':response.json()})
    elif request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        value= request.POST.get("value")
        product = {
            "name": name,
            "description": description,
            "value": value,
        }
        response = requests.put(url=f"http://localhost:8080/api/v1/products/{id}/", headers=HEADER, data=product)
        if response.status_code == 200:
            return redirect('/products/list')


def delete(request, **kwargs):
    id = kwargs.get('pk')
    if request.method == "GET":
        response = requests.get(url=f"http://localhost:8080/api/v1/products/{id}/", headers=HEADER)
        if response.status_code == 200:
            return render(request, "delete.html", {'product':response.json()})
    elif request.method == "POST":
        response = requests.delete(url=f"http://localhost:8080/api/v1/products/{id}/", headers=HEADER, data=None)
        if response.status_code == 204:
            return redirect('/products/list')
