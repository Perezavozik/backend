from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class TypeDocument(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255, verbose_name="Название"),
        description=models.TextField(verbose_name="Описание"),
    )

    order = models.PositiveSmallIntegerField(default=10, verbose_name="Сортировка")
    class Meta:
        verbose_name = "Тип документов"
        verbose_name_plural = "Типы документов"
        ordering = ("order",)

    def __str__(self) -> str:
        return self.safe_translation_getter("title", any_language=True) or "—"


class Document(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    file = models.FileField(upload_to='documents', verbose_name="Файл")
    type_document = models.ForeignKey("TypeDocument", on_delete=models.CASCADE, related_name="documents", verbose_name="Документы")

    class Meta:
        verbose_name = "Документы"
        verbose_name_plural = verbose_name

    def __str__(self) -> str:
        return self.title
