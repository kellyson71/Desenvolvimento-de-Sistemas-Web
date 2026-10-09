from django.contrib import admin

from .models import Author, Book, Category


class BookInline(admin.TabularInline):
    model = Book.authors.through
    extra = 1
    verbose_name = "livro"
    verbose_name_plural = "livros"


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "nationality")
    search_fields = ("name",)
    inlines = [BookInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "autores", "year", "available")
    search_fields = ("title", "authors__name")
    list_filter = ("available", "categories")
    filter_horizontal = ("authors", "categories")

    @admin.display(description="Autores")
    def autores(self, livro):
        return ", ".join(autor.name for autor in livro.authors.all())
