# admin.py
from django.contrib import admin
from django_ckeditor_5.widgets import CKEditor5Widget
from parler.admin import TranslatableAdmin
from parler.forms import TranslatableModelForm

from reports.models import Report


class ReportsAdminForm(TranslatableModelForm):
    class Meta:
        model = Report
        fields = '__all__'
        widgets = {
            'body': CKEditor5Widget(config_name='default'),
        }

@admin.register(Report)
class ReportsAdmin(TranslatableAdmin):
    form = ReportsAdminForm

    list_display = ('menu_title', 'title', 'order')
    list_editable = ('order',)
    list_per_page = 20
    ordering = ('order',)
    search_fields = (
        'translations__menu_title',
        'translations__title',
        'translations__body',
    )
    fieldsets = (
        (None, {
            'fields': ('menu_title', 'title', 'body'),
        }),
        ('Дополнительные параметры', {
            'fields': ('order',),
        }),
    )
