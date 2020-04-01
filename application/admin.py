from django.contrib import admin
from . import models


@admin.register(models.Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'id',
        'api_key',
        'owner',
        'is_active',
    )

