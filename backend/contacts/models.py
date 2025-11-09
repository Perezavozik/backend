from django.db import models
from solo.models import SingletonModel


class SiteContacts(SingletonModel):
    email     = models.EmailField("E-mail", blank=True)
    address   = models.CharField("Адрес", max_length=255, blank=True)
    working_time = models.TextField("Время работы", blank=True)

    class Meta:
        verbose_name = "Контакты сайта"

    def __str__(self):
        return "Контакты сайта"

class PhonesContacts(models.Model):
    site = models.ForeignKey(SiteContacts, on_delete=models.CASCADE, related_name="phones")
    phone  = models.CharField("Телефон", max_length=50, blank=True)

    def __str__(self):
        return self.phone
