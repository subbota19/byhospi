# Generated by Django 3.0.5 on 2020-04-17 19:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_auto_20200416_0759'),
        ('map', '0002_auto_20200414_1702'),
        ('client', '0003_auto_20200414_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='HosAdmin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_admin', models.BooleanField(default=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Hospital')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='map.Region')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.Status')),
            ],
            options={
                'verbose_name': 'HosAdmin',
                'verbose_name_plural': 'HosAdmin',
            },
        ),
    ]