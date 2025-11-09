from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from detail_pages_components.our_projects.models import OurProject


@receiver(post_save, sender=OurProject)
@receiver(post_delete, sender=OurProject)
def clear_our_project_gallery_cache(sender, instance, **kwargs):
    cache.delete('our_projects_gallery')
