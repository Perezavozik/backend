from django.db import models


class MediaLibrary(models.Model):
    image = models.ImageField(upload_to='media-library')

    class Meta:
        verbose_name = 'Медиатека'
        verbose_name_plural = 'Медиатека'


    def __str__(self):
        return self.image.name
