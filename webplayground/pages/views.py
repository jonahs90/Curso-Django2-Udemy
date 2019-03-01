
from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Page

# Create your views here.
class PagesListView(ListView):
    model = Page

class PagesDetailView(DetailView):
    model = Page
