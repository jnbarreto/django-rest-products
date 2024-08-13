from django.urls import path, include
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("auth/sign-in/", views.login, name="login"),

]