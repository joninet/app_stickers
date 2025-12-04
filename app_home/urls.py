
from django.urls import path
from .views.home_views import home

urlpatterns = [
    # Vista principal
    path('', home, name='home'),
]