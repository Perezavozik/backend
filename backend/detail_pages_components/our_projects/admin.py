from django.contrib import admin
from django.utils.html import format_html
from parler.admin import TranslatableAdmin

from detail_pages_components.our_projects.models import OurProject


@admin.register(OurProject)
class OurProjectAdmin(TranslatableAdmin):
    list_display = ("name", "announcement", "order")
    list_filter = ("order", )
    ordering = ("order", )
    list_editable = ("order",)
    fields = (
        "name",
        "slug",
        "announcement",
        "description",
        "image",
        "image_preview",
        "order",
    )
    readonly_fields = ('image_preview',)


    def image_preview(self, obj):
        if obj.image:  # Если изображение загружено
            return format_html('<img src="{}" style="width: 200px; height: auto;" />', obj.image.url)
        return "Нет изображения"

    image_preview.short_description = "Превью фотографии"


