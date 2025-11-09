from django.contrib import admin
from parler.admin import TranslatableAdmin

from detail_pages_components.news_on_main.models import NewsOnMain


@admin.register(NewsOnMain)
class NewsOnMainAdmin(TranslatableAdmin):
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
