from datetime import date

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
        fields = ["title", "author", "year", "available", "categories"]
        labels = {
            "title": "Título",
            "author": "Autor",
            "year": "Ano",
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
        titulo = " ".join(self.cleaned_data["title"].split())
        if len(titulo) < 3:
            raise forms.ValidationError(
                "O título precisa ter pelo menos 3 caracteres, sem contar os espaços sobrando. Escreva o título completo do livro."
            )
        return titulo

    def clean_year(self):
        ano = self.cleaned_data["year"]
        ano_atual = date.today().year
        if ano > ano_atual:
            raise forms.ValidationError(
                f"O ano não pode ser depois de {ano_atual}. Confira o ano de publicação e informe {ano_atual} ou um ano anterior."
            )
        return ano
