# Generated by Django 4.1.6 on 2023-02-03 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("endereco", "0001_initial"),
        ("carrinho", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transportadora",
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
                    "nome",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Transportadora: ",
                    ),
                ),
                (
                    "carrinho",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="carrinho.carrinho",
                        verbose_name="Carrinho: ",
                    ),
                ),
                (
                    "endereco",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="endereco.endereco",
                        verbose_name="Endereço: ",
                    ),
                ),
            ],
        ),
    ]