from django.db import models
from django.utils.text import slugify
# Create your models here.
class Content(models.Model):
    title       = models.CharField(blank=True, max_length=255)
    subtitle    = models.CharField(blank=True, max_length=255)
    cover       = models.ImageField(upload_to="cover/bootstrap/", default="default.png", blank=True)
    content     = models.TextField(blank=True)
    title1      = models.CharField(blank=True, max_length=255)
    content1    = models.TextField(blank=True)
    code1       = models.TextField(blank=True)
    text1       = models.TextField(blank=True)
    image1      = models.ImageField(upload_to="image/bootstrap/", default="default.png", blank=True)
    caption1    = models.TextField(blank=True)
    title2      = models.CharField(blank=True, max_length=255)
    content2    = models.TextField(blank=True)
    code2       = models.TextField(blank=True)
    text2       = models.TextField(blank=True)
    image2      = models.ImageField(upload_to="image/bootstrap/", default="default.png", blank=True)
    caption2    = models.TextField(blank=True)
    linkA       = models.CharField(blank=True, max_length=255)
    linkB       = models.CharField(blank=True, max_length=255)
    linkC       = models.CharField(blank=True, max_length=255)
    linkD       = models.CharField(blank=True, max_length=255)
    linkE       = models.CharField(blank=True, max_length=255)
    linkF       = models.CharField(blank=True, max_length=255)
    linkG       = models.CharField(blank=True, max_length=255)
    CATEGORY    = (
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
