# Generated by Django 4.1.6 on 2023-02-06 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("item", "0001_initial"),
        ("locador", "0004_remove_locador_itens_escolhidos_locador_produto_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="locador",
            name="produto",
        ),
        migrations.AddField(
            model_name="locador",
            name="produto",
            field=models.ManyToManyField(
                blank=True, null=True, to="item.item", verbose_name="lista de itens:"
            ),
        ),
    ]