
from django.urls import path, include
from .views.home_views import home

urlpatterns = [
    # Vista principal
    path('', home, name='home'),
    path('store/', include('store.urls')),
    path('cart/', include('carts.urls')),
]