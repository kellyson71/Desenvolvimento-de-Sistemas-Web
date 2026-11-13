import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("biblioteca", "0002_relacionamentos"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="books",
                to="biblioteca.author",
                verbose_name="autor",
            ),
        ),
        migrations.AddField(
            model_name="book",
            name="authors",
            field=models.ManyToManyField(
                related_name="books_novo",
                to="biblioteca.author",
                verbose_name="autores",
            ),
        ),
    ]
