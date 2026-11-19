from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView

from .forms import AuthorForm, BookForm
from .models import Author, Book


class BookListView(ListView):
    model = Book
    template_name = "biblioteca/lista_livros.html"
    context_object_name = "livros"

    def get_queryset(self):
        return Book.objects.select_related("author").order_by("title")


class BookDetailView(DetailView):
    model = Book
    template_name = "biblioteca/book_detail.html"
    context_object_name = "livro"


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "biblioteca/book_form.html"
    extra_context = {"titulo": "Novo livro", "botao": "Cadastrar livro"}

    def get_success_url(self):
        return reverse("biblioteca:author_detail", kwargs={"pk": self.object.author_id})


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "biblioteca/book_form.html"
    extra_context = {"titulo": "Editar livro", "botao": "Salvar alterações"}

    def get_success_url(self):
        return reverse("biblioteca:author_detail", kwargs={"pk": self.object.author_id})


class BookDeleteView(DeleteView):
    model = Book
    template_name = "biblioteca/livro_confirm_delete.html"
    context_object_name = "livro"
    success_url = reverse_lazy("biblioteca:listar_livros")


class AuthorDetailView(DetailView):
    model = Author
    template_name = "biblioteca/author_detail.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["livros"] = self.object.books.all()
        return contexto


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = "biblioteca/author_form.html"

    def get_success_url(self):
        return reverse("biblioteca:author_detail", kwargs={"pk": self.object.pk})


class SobreView(TemplateView):
    template_name = "biblioteca/sobre.html"

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["total"] = Book.objects.count()
        contexto["disponiveis"] = Book.objects.filter(available=True).count()
        return contexto
