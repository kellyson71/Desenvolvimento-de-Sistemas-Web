from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("biblioteca", "0004_copiar_autores"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="author",
        ),
        migrations.AlterField(
            model_name="book",
            name="authors",
            field=models.ManyToManyField(
                related_name="books",
                to="biblioteca.author",
                verbose_name="autores",
            ),
        ),
    ]
