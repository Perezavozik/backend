from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import PhonesContacts, SiteContacts


class PhonesContactsInline(admin.TabularInline):
    model = PhonesContacts
    extra = 1
    verbose_name = "Телефон"
    verbose_name_plural = "Телефоны"


@admin.register(SiteContacts)
class SiteContactsAdmin(SingletonModelAdmin):
    """Admin interface for SiteContacts singleton."""
    inlines = [PhonesContactsInline]

    fieldsets = (
        (None, {
            'fields': ('email', 'address', 'working_time'),
            'description': 'Основные контактные данные сайта',
        }),
    )

    # list_display не может содержать phone, т.к. его нет в SiteContacts
    list_display = ('email', 'address')
