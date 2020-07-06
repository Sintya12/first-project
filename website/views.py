from django.shortcuts import render
from django.views.generic import TemplateView
from blog.views import ContentList
class Tutorial(TemplateView):
    template_name = "tutor.html"
class Home(TemplateView, ContentList):
    template_name = "home.html"
    def get_context_data(self):
        querysets = self.get_latest_konten()
        context = {
            'latest_content':querysets,
        }
        return context
