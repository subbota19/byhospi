from django.contrib import admin
from client.models import Comment, Client, Status


class AdminClient(admin.ModelAdmin):
    list_display = ['id', 'username', 'confirmed', 'email', 'updated', 'status']


class AdminComment(admin.ModelAdmin):
    list_display = ['id', 'description', 'client_hospital', 'hospital_client']


class AdminStatus(admin.ModelAdmin):
    list_display = ['id', 'position']


admin.site.register(Status, AdminStatus)
admin.site.register(Client, AdminClient)
admin.site.register(Comment, AdminComment)
