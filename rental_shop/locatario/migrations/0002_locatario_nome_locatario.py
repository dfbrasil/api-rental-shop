# Generated by Django 4.1.6 on 2023-02-06 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("usuario", "0001_initial"),
        ("locatario", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="locatario",
            name="nome_locatario",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="usuario.usuario",
                verbose_name="nome do usuário: ",
            ),
        ),
    ]
