from django.db import models

from hospital.models import Hospital
from map.models import Region


class Status(models.Model):
    id = models.AutoField(primary_key=True)
    position = models.CharField(max_length=40)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuses"


class HosAdmin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=15, null=False)
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=True)
    confirmed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "HosAdmin"
        verbose_name_plural = "HosAdmin"


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=15, null=False)
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)

    mtm_comment = models.ManyToManyField(Hospital, through="Comment")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    client_hospital = models.ForeignKey(Client, on_delete=models.CASCADE)
    hospital_client = models.ForeignKey(Hospital, on_delete=models.CASCADE)

    def __str__(self):
        return self.client_hospital.username

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
