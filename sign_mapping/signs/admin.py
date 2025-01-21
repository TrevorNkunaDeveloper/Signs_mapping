from django.contrib import admin
from .models import Sign

@admin.register(Sign)
class SignAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'date_taken', 'last_updated')