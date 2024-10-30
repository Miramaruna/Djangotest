from django.contrib import admin
from app.models import Main

# Register your models here.

@admin.register(Main)
class EventAdmin(admin.ModelAdmin):
    fields = ['Name', 'Text']
    # readonly_fields = ['date']