from django.db import models

class News(models.Model):
    title = models.TextField()
    text = models.TextField()
    url = models.TextField()
    tags = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'