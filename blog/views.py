from django.shortcuts import render
from django.views.generic import ListView,DetailView

from .models import *
# Create your views here.
class ContentList():
    model = Content
    def get_latest_konten(self):
        list_content = self.model.objects.values_list('title', flat=True).distinct()
        queryset = []
        for content in list_content :
            content = self.model.objects.filter(title=content).latest('publish')
            queryset.append(content)
        return queryset
        
class Page(ListView):
    model               = Content
    template_name       = 'blog/content_list.html'
    context_object_name = 'content_list'
class ContentDetail(DetailView):
    model               = Content
    template_name       = 'blog/content_detail.html'
    context_object_name = 'content'
    def get_context_data(self, *args, **kwargs):
        other_content = self.model.objects.filter(category = self.object.category).distinct().exclude(id = self.object.id)
        self.kwargs.update({'other_content':other_content})
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)
