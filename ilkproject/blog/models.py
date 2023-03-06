from django.db import models
from django.utils.text import slugify


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=128)
    image = models.CharField(max_length=64)
    description = models.TextField(null=True)
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, unique=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.title), allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"


class Category(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(blank=True, unique=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.name), allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
