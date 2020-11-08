from django.contrib import admin

from map.models import Region


class AdminRegion(admin.ModelAdmin):
    list_display = ["id", "name", "population"]


admin.site.register(Region, AdminRegion)
