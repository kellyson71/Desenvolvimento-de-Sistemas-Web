from django.shortcuts import get_object_or_404, redirect, render

from .forms import AuthorForm
from .models import Author, Book


def listar_livros(request):
    livros = Book.objects.prefetch_related("authors")
    return render(request, "biblioteca/lista_livros.html", {"livros": livros})


def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, "biblioteca/author_detail.html", {"author": author, "livros": author.books.all()})


def author_create(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            return redirect("biblioteca:author_detail", pk=author.pk)
    else:
        form = AuthorForm()
    return render(request, "biblioteca/author_form.html", {"form": form})
