from django.db import models


class Partners(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    image = models.ImageField(upload_to='partners/', verbose_name="Фотография")
    order = models.PositiveSmallIntegerField(default=1, verbose_name="Сортировка")

    class Meta:
        db_table = 'Галерея партнеров'
        verbose_name = "Компания партнер"
        verbose_name_plural = "Компании партнеры"

    def __str__(self):
        return self.name
