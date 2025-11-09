from django.contrib import admin
from django.utils.html import format_html

from content_list.partners.models import Partners


@admin.register(Partners)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    list_filter = ("name", "order")
    search_fields = ("name",)
    ordering = ("order",)
    list_editable = ("order",)
    fields = ("name", "image", "image_preview", "order")
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:  # Если изображение загружено
            return format_html('<img src="{}" style="width: 200px; height: auto;" />', obj.image.url)
        return "Нет изображения"

    image_preview.short_description = "Превью фотографии"
