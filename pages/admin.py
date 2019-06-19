from django.contrib import admin
from .models import EnergyUsage

class EnergyUsageAdmin(admin.ModelAdmin):
    list_display = ['id', 'current', 'voltage', 'watt', 'cdate', 'ctime']

admin.site.register(EnergyUsage, EnergyUsageAdmin);
