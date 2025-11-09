from django.apps import AppConfig


class OurProjectsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "detail_pages_components.our_projects"
    verbose_name = "Наши проекты"

    def ready(self):
        pass
