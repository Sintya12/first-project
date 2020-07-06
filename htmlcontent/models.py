from django.db import models
from django.utils.text import slugify

# Create your models here.
class Content(models.Model):
    title1      = models.CharField(blank=True, max_length=255)
    cover       = models.ImageField(upload_to="cover/html/", default="default.png", blank=True)
    text1       = models.TextField(blank=True)
    title2      = models.CharField(blank=True, max_length=255)
    text2       = models.TextField(blank=True)
    title3      = models.CharField(blank=True, max_length=255)
    text3       = models.TextField(blank=True)
    title4      = models.CharField(blank=True, max_length=255)
    text4       = models.TextField(blank=True)
    title5      = models.CharField(blank=True, max_length=255)
    text5       = models.TextField(blank=True)
    title6      = models.CharField(blank=True, max_length=255)
    text6       = models.TextField(blank=True)

    code        = models.TextField(blank=True)
    text        = models.TextField(blank=True)
    image       = models.ImageField(upload_to="image/html/", default="default.png", blank=True)
    caption     = models.TextField(blank=True)

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
        self.slug = slugify(self.title1)
        super().save()

    def __str__(self):
        return "{}.{}".format(self.id, self.title1)
