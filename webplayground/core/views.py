from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title':"WEB PLAYGROUND 3.0"})

class SamplePageView(TemplateView):
    template_name = "core/sample.html"
