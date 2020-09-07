from django.contrib import admin
from . import models


@admin.register(models.Havior)
class HaviorAdmin(admin.ModelAdmin):
    pass