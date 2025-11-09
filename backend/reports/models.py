from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from parler.models import TranslatableModel, TranslatedFields


class Report(TranslatableModel):
    translations = TranslatedFields(
        menu_title=models.CharField(max_length=255, verbose_name='Заголовок в меню'),
        title=models.CharField(max_length=255, verbose_name='Заголовок'),
        body=CKEditor5Field('Текст', config_name='default'),
    )
    order = models.PositiveSmallIntegerField(default=10, verbose_name='Сортировка')

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'

    def __str__(self):
        return self.safe_translation_getter('menu_title', any_language=True)
