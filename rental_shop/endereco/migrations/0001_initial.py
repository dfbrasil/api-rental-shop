# Generated by Django 4.1.6 on 2023-02-06 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Endereco",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "logradouro",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Rua/Avenida: ",
                    ),
                ),
                (
                    "cidade",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Cidade: "
                    ),
                ),
                (
                    "estado",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="Estado: "
                    ),
                ),
                (
                    "pais",
                    models.CharField(
                        blank=True, max_length=50, null=True, verbose_name="País: "
                    ),
                ),
            ],
        ),
    ]
