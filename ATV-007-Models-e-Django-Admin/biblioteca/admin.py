from django.contrib import admin

from .models import Livro


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "ano_publicacao", "disponivel")
    list_filter = ("disponivel",)
    search_fields = ("titulo", "autor")
