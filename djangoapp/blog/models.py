from django.db import models
from utils.rands import slugify_new


# Create your models here.
class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=255)
    slug = models.SlugField(
        unique=True, default=None,
        null=True, blank=True
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name, 10)
        return super().save(*args, **kwargs)
