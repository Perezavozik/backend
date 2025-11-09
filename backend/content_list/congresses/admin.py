# admin.py
from django.contrib import admin
from django_ckeditor_5.widgets import CKEditor5Widget
from parler.admin import TranslatableAdmin
from parler.forms import TranslatableModelForm

from .models import Congresses


class CongressesAdminForm(TranslatableModelForm):
    class Meta:
        model = Congresses
        fields = '__all__'
        widgets = {
            'body': CKEditor5Widget(config_name='default'),
        }

@admin.register(Congresses)
class CongressesAdmin(TranslatableAdmin):
    form = CongressesAdminForm

    list_display    = ('id', 'menu_title', 'title', 'order')
    list_editable   = ('order',)
    list_per_page   = 20
    ordering        = ('order',)
    search_fields   = ('menu_title', 'title')
    fieldsets = (
        (None, {
            'fields': ('menu_title', 'title', 'body'),
        }),
        ('Контент', {
            'fields': ('order',),
        }),
    )
