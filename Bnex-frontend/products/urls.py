from django.urls import path, include
from . import views

urlpatterns = [
    path("list/", views.list, name="list"),
    path("detail/<int:pk>", views.detail, name="detail"),
    path("delete/<int:pk>", views.delete, name="delete"),
    path("update/<int:pk>", views.update, name="update"),
    path("create/", views.create, name="create"),

]