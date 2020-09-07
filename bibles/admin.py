from django.contrib import admin
from . import models


@admin.register(models.Bible)
class BibleAdmin(admin.ModelAdmin):
    pass