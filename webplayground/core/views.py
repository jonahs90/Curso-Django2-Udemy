from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "WEB PLAYGROUND 2.0"
        return context

    def get(self, request):
        return render(request, self.template_name, {'title':"WEB PLAYGROUND 3.0"})
class SamplePageView(TemplateView):
    template_name = "core/sample.html"
