from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from parler.models import TranslatableModel, TranslatedFields
from slugify import slugify as ascii_slugify

from search.handler import SearchableMixin


class Society(SearchableMixin, TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=100, verbose_name="Название"),
        announcement=models.TextField(verbose_name="Анонс"),
        description=CKEditor5Field('Текст', config_name='default'),
    )
    slug = models.SlugField(verbose_name="Символьный код", blank=True, unique=True)
    image = models.ImageField(upload_to="our_projects/", verbose_name="Фотография", blank=True, null=True)
    order = models.PositiveIntegerField(default=1, verbose_name="Сортировка")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Общество"
        verbose_name_plural = "Общество"

    def save(self, *args, **kwargs):
        if not self.slug:
            name = self.safe_translation_getter('name') or ''
            base = ascii_slugify(name) or 'item'

            max_len = self._meta.get_field('slug').max_length or 50
            slug = base[:max_len]
            i = 2
            qs = type(self).objects.all()
            if self.pk:
                qs = qs.exclude(pk=self.pk)
            while qs.filter(slug=slug).exists():
                suffix = f'-{i}'
                slug = f"{base[:max_len - len(suffix)]}{suffix}"
                i += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.safe_translation_getter('name', any_language=True)
