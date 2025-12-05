from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import SubCategory 

def store(request, subcategory_slug=None):
    subcategories = None
    
    if subcategory_slug:
        subcategories = get_object_or_404(SubCategory, slug=subcategory_slug)
        products = Product.objects.filter(subcategory=subcategories, is_available=True)
    else:
        products = Product.objects.filter(is_available=True)

    product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count
    }
    
    return render(request, 'store/store.html', context)


