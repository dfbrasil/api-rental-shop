# Generated by Django 4.1.6 on 2023-02-04 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("item", "0007_delete_itempedido"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="quantidade_restante",
        ),
        migrations.AddField(
            model_name="item",
            name="quantidade_pedida",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Quantidade de itens pedidos"
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="quantidade",
            field=models.IntegerField(
                blank=True, default=0, null=True, verbose_name="Quantidade de itens"
            ),
        ),
    ]