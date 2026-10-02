from django.urls import path

from . import views

app_name = "biblioteca"

urlpatterns = [
    path("", views.listar_livros, name="listar_livros"),
]
