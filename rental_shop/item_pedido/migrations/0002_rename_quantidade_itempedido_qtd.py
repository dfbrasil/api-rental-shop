# Generated by Django 4.1.6 on 2023-02-03 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item_pedido', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itempedido',
            old_name='quantidade',
            new_name='qtd',
        ),
    ]