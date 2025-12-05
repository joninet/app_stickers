from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('<slug:subcategory_slug>', views.store, name='products_by_subcategory')
]
