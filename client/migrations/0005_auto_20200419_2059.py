# Generated by Django 3.0.5 on 2020-04-19 20:59
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("client", "0004_auto_20200417_1935"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="hosadmin",
            name="hospital",
        ),
        migrations.RemoveField(
            model_name="hosadmin",
            name="region",
        ),
    ]
