from django.contrib import admin
# Register your models here.
from .models import *
class ContentAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
        'publish',
    ]
admin.site.register(Content, ContentAdmin)
