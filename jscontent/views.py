from django.shortcuts import render
from django.views.generic import ListView,DetailView
# Create your views here.
from .models import *
class Page(ListView):
    model = Content
    template_name= 'javascript/page_list.html'
    context_object_name = 'content_list'
class ContentList(ListView):
    model = Content
    template_name= 'javascript/content_list.html'
    context_object_name = 'content_list'
class ContentDetail(DetailView):
    model = Content
    template_name = 'javascript/content_detail.html'
    context_object_name = 'content'
    def get_context_data(self, *args, **kwargs):
        other_content = self.model.objects.filter(category = self.object.category).distinct().exclude(id = self.object.id)
        self.kwargs.update({'other_content':other_content})
        kwargs = self.kwargs
        return super().get_context_data(*args, **kwargs)
