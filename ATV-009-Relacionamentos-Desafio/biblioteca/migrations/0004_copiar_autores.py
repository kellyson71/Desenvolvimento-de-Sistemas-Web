from django.db import migrations


def copiar_autor(apps, schema_editor):
    Book = apps.get_model("biblioteca", "Book")
    for livro in Book.objects.all():
        livro.authors.add(livro.author)


def desfazer(apps, schema_editor):
    Book = apps.get_model("biblioteca", "Book")
    for livro in Book.objects.all():
        livro.author = livro.authors.first()
        livro.save()


class Migration(migrations.Migration):

    dependencies = [
        ("biblioteca", "0003_book_authors"),
    ]

    operations = [
        migrations.RunPython(copiar_autor, desfazer),
    ]
