from django.contrib import admin

from client.models import Client
from client.models import Comment
from client.models import HosAdmin
from client.models import Status


class AdminClient(admin.ModelAdmin):
    list_display = ["id", "username", "confirmed", "email", "updated", "status"]


class AdminHosAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "confirmed", "email", "updated", "status"]


class AdminComment(admin.ModelAdmin):
    list_display = ["id", "description", "client_hospital", "hospital_client"]
    list_filter = ["client_hospital", "hospital_client"]


class AdminStatus(admin.ModelAdmin):
    list_display = ["id", "position"]


admin.site.register(Status, AdminStatus)
admin.site.register(Client, AdminClient)
admin.site.register(Comment, AdminComment)
admin.site.register(HosAdmin, AdminHosAdmin)
