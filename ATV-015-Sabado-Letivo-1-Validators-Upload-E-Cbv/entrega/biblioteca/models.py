from django.core.exceptions import ValidationError
from django.core.validators import (
    FileExtensionValidator,
    MaxValueValidator,
    MinLengthValidator,
    MinValueValidator,
    RegexValidator,
)
from django.db import models

from .validators import validar_ano_publicacao, validar_tamanho_arquivo


class Author(models.Model):
    name = models.CharField(max_length=120)
    nationality = models.CharField(max_length=60, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Autor"
        verbose_name_plural = "autores"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(
        "título",
        max_length=200,
        validators=[
            MinLengthValidator(3, "O título precisa ter pelo menos 3 caracteres. Escreva o título completo do livro."),
        ],
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.PROTECT,
        related_name="books",
        verbose_name="autor",
    )
    categories = models.ManyToManyField(
        Category,
        blank=True,
        related_name="books",
        verbose_name="categorias",
    )
    year = models.IntegerField("ano de publicação", validators=[validar_ano_publicacao])
    pages = models.PositiveIntegerField(
        "páginas",
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1, "O livro precisa ter pelo menos 1 página."),
            MaxValueValidator(5000, "O número de páginas não pode passar de 5000."),
        ],
    )
    isbn = models.CharField(
        "ISBN",
        max_length=13,
        blank=True,
        validators=[RegexValidator(r"^\d{13}$", "O ISBN precisa ter exatamente 13 dígitos, só números.")],
    )
    capa = models.ImageField(
        "capa",
        upload_to="capas/",
        blank=True,
        validators=[
            validar_tamanho_arquivo,
            FileExtensionValidator(["jpg", "jpeg", "png"], "Envie a capa em jpg, jpeg ou png."),
        ],
    )
    available = models.BooleanField("disponível", default=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

    def clean(self):
        erros = {}
        if self.author_id and self.title.strip().casefold() == self.author.name.strip().casefold():
            erros["title"] = "O título não pode ser igual ao nome do autor."
        if not self.available and not self.isbn:
            erros["isbn"] = "Um livro indisponível precisa ter o ISBN preenchido."
        if erros:
            raise ValidationError(erros)

    def __str__(self):
        return f"{self.title} ({self.year})"
