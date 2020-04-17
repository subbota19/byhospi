from django.db import models
from map.models import Region


class Hospital(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=False, null=False)
    full_address = models.CharField(max_length=150, unique=False, null=False)
    need_help = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True, default=None)

    location = models.ForeignKey(Region, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Hospital'
        verbose_name_plural = 'Hospitals'


class Number(models.Model):
    id = models.AutoField(primary_key=True)
    number_phone = models.CharField(max_length=25, unique=False, null=True)

    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.number_phone

    class Meta:
        verbose_name = 'Number'
        verbose_name_plural = 'Numbers'
