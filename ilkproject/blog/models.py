from hashlib import sha256, md5
from django.db import models
from django.utils.text import slugify


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=128)
    image = models.ImageField(upload_to="blogs")
    description = models.TextField(null=True)
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, unique=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        # md = md5((self.title+"lib").encode('utf-8'))
        md2 = sha256((self.title+"lib").encode('utf-8'))
        self.slug = slugify(md2.hexdigest())
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"


class Category(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(blank=True, unique=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        # md = md5((self.name+"lib").encode('utf-8'))
        md2 = sha256((self.name+"lib").encode('utf-8'))
        self.slug = slugify(md2.hexdigest())
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
