from django.contrib import admin
from apps.main.models import Main

# Register your models here.

@admin.register(Main)
class EventAdmin(admin.ModelAdmin):
    fields = ['Name', 'Text']
    # readonly_fields = ['date']