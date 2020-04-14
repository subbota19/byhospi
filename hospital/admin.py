from django.contrib import admin
from hospital.models import Hospital, Number


class AdminHospital(admin.ModelAdmin):
    list_display = ['id', 'name', 'full_address', 'location']


class AdminNumber(admin.ModelAdmin):
    list_display = ['id', 'number_phone', 'hospital']


admin.site.register(Hospital, AdminHospital)
admin.site.register(Number, AdminNumber)
