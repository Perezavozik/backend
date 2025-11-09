from django.contrib import admin
from parler.admin import TranslatableAdmin

from documents.models import Document, TypeDocument


class DocumentInline(admin.TabularInline):
    model = Document
    extra = 1
    fields = ('title', 'file')

@admin.register(TypeDocument)
class TypeDocumentAdmin(TranslatableAdmin):
    list_display       = ("title", "description", "order")
    list_editable      = ("order",)
    ordering           = ("order",)
    search_fields      = ("translations__title", "translations__description")
    translation_fields = ("title", "description")
    inlines            = [DocumentInline]

    fieldsets = (
        (None, {"fields": ("title", "description", "order")}),
    )
