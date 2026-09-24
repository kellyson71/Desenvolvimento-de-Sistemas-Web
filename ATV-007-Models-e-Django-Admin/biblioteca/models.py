from django.db import models


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=120)
    ano_publicacao = models.IntegerField()
    disponivel = models.BooleanField(default=True)

    class Meta:
        ordering = ["titulo"]
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

    def __str__(self):
        return f"{self.titulo} ({self.ano_publicacao})"
