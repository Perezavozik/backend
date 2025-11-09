from django.contrib import admin
from parler.admin import TranslatableAdmin

from detail_pages_components.history.models import History


@admin.register(History)
class HistoryAdmin(TranslatableAdmin):
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
