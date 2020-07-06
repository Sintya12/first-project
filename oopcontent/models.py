from django.db import models
from django.utils.text import slugify
# Create your models here.
class Content(models.Model):
    title       = models.CharField(blank=True, max_length=255)
    subtitle    = models.CharField(blank=True, max_length=255)
    cover       = models.ImageField(upload_to="cover/oop/", default="default.png", blank=True)
    content     = models.TextField(blank=True)
    title1      = models.CharField(blank=True, max_length=255)
    content1    = models.TextField(blank=True)
    title2      = models.CharField(blank=True, max_length=255)
    content2    = models.TextField(blank=True)
    title3     = models.CharField(blank=True, max_length=255)
    content3   = models.TextField(blank=True)
    code3      = models.TextField(blank=True)
    text3      = models.TextField(blank=True)
    title4     = models.CharField(blank=True, max_length=255)
    content4   = models.TextField(blank=True)
    code4      = models.TextField(blank=True)
    text4      = models.TextField(blank=True)
    title5     = models.CharField(blank=True, max_length=255)
    content5   = models.TextField(blank=True)
    code5      = models.TextField(blank=True)
    text5      = models.TextField(blank=True)
    code6      = models.TextField(blank=True)
    caption5   = models.TextField(blank=True)
    CATEGORY   = (
                    ('html','html'),
                    ('css','css'),
                    ('js','js'),
                    ('dom','dom'),
                    ('bootstrap','bootstrap'),
                    ('python','python'),
                    ('oop','oop'),
                    ('django','django'),
                  )
    category    = models.CharField(max_length=255, choices=CATEGORY)
    author      = models.CharField(max_length=255)
    publish     = models.DateTimeField(auto_now_add=True)
    slug        = models.SlugField(blank=True, editable=False)
    def save(self):
        self.slug = slugify(self.title)
        super().save()
    def __str__(self):
        return "{}.{}".format(self.id, self.title)
