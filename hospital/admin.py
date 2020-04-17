from django.contrib import admin
from hospital.models import Hospital, Number


class AdminHospital(admin.ModelAdmin):
    list_display = ['id', 'name', 'full_address', 'location', 'phone_number']
    search_fields = ['name', 'full_address']
    list_filter = ['location']

    @staticmethod
    def phone_number(obj):
        return ','.join(x.number_phone for x in obj.number_set.all() if x.number_phone)


class AdminNumber(admin.ModelAdmin):
    list_display = ['id', 'number_phone', 'hospital']


admin.site.register(Hospital, AdminHospital)
admin.site.register(Number, AdminNumber)
