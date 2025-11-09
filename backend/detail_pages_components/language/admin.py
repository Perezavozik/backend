from django.contrib import admin
from parler.admin import TranslatableAdmin

from detail_pages_components.language.models import Language


@admin.register(Language)
class LanguageAdmin(TranslatableAdmin):
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
