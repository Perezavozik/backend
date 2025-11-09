# admin.py
from django.contrib import admin

from .models import FeedbackForm


@admin.register(FeedbackForm)
class FeedbackFormAdmin(admin.ModelAdmin):
    # колонки в списке
    list_display = (
        "id",
        "created_at",
        "name",
        "email",
        "phone",
        "active",
        "short_message",
    )
    # ссылки-на-редактирование
    list_display_links = ("id", "name")
    # фильтры справа
    list_filter = ("active", "created_at")
    # поиск
    search_fields = ("name", "email", "phone", "message")
    # сортировка по умолчанию (новые сверху)
    ordering = ("-created_at",)
    # навигация по дате сверху
    date_hierarchy = "created_at"
    # только для чтения в форме
    readonly_fields = ("created_at",)

    def short_message(self, obj):
        """Сокращённое сообщение в списке (до 50 симв.)."""
        return (obj.message[:50] + "…") if len(obj.message) > 50 else obj.message
    short_message.short_description = "Сообщение"
