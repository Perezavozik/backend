from django.contrib import admin
from parler.admin import TranslatableAdmin

from detail_pages_components.events.models import Event


@admin.register(Event)
class EventAdmin(TranslatableAdmin):
    list_display = ('name', 'date', 'place', 'order')
    list_filter = ('date', 'place')
    search_fields = ('name', 'announcement', 'description')
    fieldsets = (
        (None, {
            'fields': ('name', 'announcement', 'description'),
        }),
        ('Дополнительные параметры', {
            'fields': ('image', 'date', 'place', 'order', 'slug'),
        }),
    )
