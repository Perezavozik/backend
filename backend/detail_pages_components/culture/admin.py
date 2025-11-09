from django.contrib import admin
from parler.admin import TranslatableAdmin

from detail_pages_components.culture.models import Culture


@admin.register(Culture)
class CultureAdmin(TranslatableAdmin):
    list_display = ("name", "order")
    search_fields = ("name", "announcement", "description")
    fieldsets = (
        (None, {
            "fields": ("name", "announcement", "description"),
        }),
        ("Дополнительные параметры", {
            "fields": ("image", "order", "slug"),
        }),
    )
