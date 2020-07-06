from django.db import models
from django.utils.text import slugify
# Create your models here.
class Content(models.Model):
    title       = models.CharField(blank=True, max_length=255)
    subtitle    = models.CharField(blank=True, max_length=255)
    cover       = models.ImageField(upload_to="cover/blog/", default="default.png", blank=True)
    content     = models.TextField(blank=True)
    title1      = models.CharField(blank=True, max_length=255)
    content1    = models.TextField(blank=True)
    title2      = models.CharField(blank=True, max_length=255)
    content2    = models.TextField(blank=True)
    title3     = models.CharField(blank=True, max_length=255)
    content3   = models.TextField(blank=True)
    category    = models.CharField(max_length=255)
    author      = models.CharField(max_length=255)
    publish     = models.DateTimeField(auto_now_add=True)
    slug        = models.SlugField(blank=True, editable=False)
    def save(self):
        self.slug = slugify(self.title)
        super().save()
    def __str__(self):
        return "{}.{}".format(self.id, self.title)
