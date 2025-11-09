from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from parler.models import TranslatableModel, TranslatedFields
from slugify import slugify as ascii_slugify


class CandidateAwards(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=100, verbose_name="Название"),
        description=CKEditor5Field('Текст', config_name='default'),
    )
    slug = models.SlugField(verbose_name="Символьный код", blank=True, unique=True, null=True)
    image = models.ImageField(upload_to='awards_candidate/%Y/%m/%d/', verbose_name="Фото")

    class Meta:
        verbose_name = "Премия"
        verbose_name_plural = "Премия"

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


class Candidate(models.Model):
    name = models.CharField(max_length=255, verbose_name="ФИО")
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(upload_to="candidates", verbose_name="Фото")
    number_of_votes = models.IntegerField(default=0, verbose_name="Количество голосов")
    awards = models.ForeignKey(CandidateAwards, related_name="candidates", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Кандидат"
        verbose_name_plural = "Кандидаты"

    def __str__(self):
        return self.name
