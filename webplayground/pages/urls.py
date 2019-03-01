from django.urls import path
from .views import PagesListView, PagesDetailView

urlpatterns = [
    path('', PagesListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PagesDetailView.as_view(), name='page'),
]