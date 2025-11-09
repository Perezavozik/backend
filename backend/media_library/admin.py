from django import forms
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.forms.widgets import ClearableFileInput

from media_library.models import MediaLibrary


class MultiClearableFileInput(ClearableFileInput):
    allow_multiple_selected = True
    needs_multipart_form = True

    def __init__(self, attrs=None, **kwargs):
        super().__init__(attrs or {}, **kwargs)
        self.attrs["multiple"] = True

    def value_from_datadict(self, data, files, name):
        return files.getlist(name)


class MultiFileField(forms.FileField):
    widget = MultiClearableFileInput

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("validators", [
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png"])
        ])
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        files = data or []
        if self.required and not files:
            raise ValidationError(self.error_messages["required"], code="required")

        # проверка каждого файла валидаторами
        for f in files:
            for validator in self.validators:
                validator(f)

        return files


class MultiImageAdminForm(forms.ModelForm):
    image = MultiFileField(
        label="Изображения",
        help_text="Можно выбрать сразу несколько файлов. (jpg, jpeg, png)",
        required=True,
    )

    class Meta:
        model = MediaLibrary
        fields = ("image",)


@admin.register(MediaLibrary)
class MediaLibraryAdmin(admin.ModelAdmin):
    form = MultiImageAdminForm
    fields = ("image",)

    def save_model(self, request, obj, form, change):
        if not change:
            files = form.cleaned_data.get("image") or []
            for f in files:
                obj.pk = None
                obj.image = f
                super().save_model(request, obj, form, change=False)
        else:
            super().save_model(request, obj, form, change)
