from django.urls import path, include
from .views import template_view, TemplView
urlpatterns = [
    path('', TemplView.as_view(), name='index'),
]
