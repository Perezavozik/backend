from django.contrib import admin
from parler.admin import TranslatableAdmin

from .models import Award


@admin.register(Award)
class AwardsAdmin(TranslatableAdmin):
    list_display = ('name', 'order')
    search_fields = ('name', 'announcement', 'description')
    fieldsets = (
        (None, {
            'fields': ('name', 'announcement', 'description'),
        }),
        ('Дополнительные параметры', {
            'fields': ('image', 'order', 'slug'),
        }),
    )
