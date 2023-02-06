# Generated by Django 4.1.6 on 2023-02-06 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuario", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="tipo",
            field=models.CharField(
                blank=True,
                choices=[(1, "Locador"), (2, "Locatário")],
                max_length=20,
                null=True,
                verbose_name="Tipo do Usuário",
            ),
        ),
    ]
