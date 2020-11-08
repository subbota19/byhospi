# Generated by Django 3.0.5 on 2020-04-14 12:17
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("map", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Hospital",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("full_address", models.CharField(max_length=150)),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="map.Region"
                    ),
                ),
            ],
            options={
                "verbose_name": "Hospital",
                "verbose_name_plural": "Hospitals",
            },
        ),
        migrations.CreateModel(
            name="Number",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("number_phone", models.CharField(max_length=25, null=True)),
                (
                    "hospital",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hospital.Hospital",
                    ),
                ),
            ],
            options={
                "verbose_name": "Number",
                "verbose_name_plural": "Numbers",
            },
        ),
    ]
