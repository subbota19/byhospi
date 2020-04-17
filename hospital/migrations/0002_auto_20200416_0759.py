# Generated by Django 3.0.5 on 2020-04-16 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='description',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='hospital',
            name='need_help',
            field=models.BooleanField(default=False),
        ),
    ]