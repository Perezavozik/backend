from django.db import models


class TelegramPost(models.Model):
    channel = models.CharField(max_length=255, db_index=True)
    post_id = models.BigIntegerField(db_index=True)
    text = models.TextField()
    post_url = models.URLField()
    photo = models.ImageField(upload_to="telegram_posts/", blank=True, null=True)
    photo_url = models.URLField(blank=True)
    photo_source_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("channel", "post_id")


    def __str__(self):
        return self.text
