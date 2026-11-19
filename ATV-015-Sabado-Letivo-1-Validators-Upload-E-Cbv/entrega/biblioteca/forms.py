from django import forms

from .models import Author, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "nationality"]
        labels = {
            "name": "Nome",
            "nationality": "Nacionalidade",
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "year", "pages", "isbn", "capa", "available", "categories"]
        labels = {
            "title": "Título",
            "author": "Autor",
            "year": "Ano",
            "pages": "Páginas",
            "isbn": "ISBN",
            "capa": "Capa",
            "available": "Disponível",
            "categories": "Categorias",
        }
        widgets = {
            "categories": forms.CheckboxSelectMultiple,
        }
        error_messages = {
            "author": {
                "required": "Escolha o autor do livro. Se ele ainda não existe, cadastre em \"Novo autor\" primeiro.",
            },
            "year": {
                "required": "Informe o ano de publicação.",
                "invalid": "O ano precisa ser um número inteiro, por exemplo 1899.",
            },
        }

    def clean_title(self):
        return " ".join(self.cleaned_data["title"].split())
