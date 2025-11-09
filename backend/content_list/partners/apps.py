from django.apps import AppConfig


class PartnersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'content_list.partners'
    verbose_name = "Галерея партнеров"

    def ready(self):
        pass
