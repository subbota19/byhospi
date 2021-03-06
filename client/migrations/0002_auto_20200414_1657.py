# Generated by Django 3.0.5 on 2020-04-14 16:57
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("client", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="client",
            options={"verbose_name": "Client", "verbose_name_plural": "Clients"},
        ),
        migrations.AddField(
            model_name="status",
            name="confirmed",
            field=models.BooleanField(default=False),
        ),
    ]
