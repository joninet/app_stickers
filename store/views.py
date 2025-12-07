from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category, SubCategory 

def store(request, category_slug=None, subcategory_slug=None):
    categories = Category.objects.all()
    current_category = None
    current_subcategory = None
    
    if subcategory_slug:
        current_subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
        current_category = current_subcategory.category
        products = Product.objects.filter(subcategory=current_subcategory, is_available=True)
    elif category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        # Filtrar productos que tengan subcategorías de esta categoría
        products = Product.objects.filter(subcategory__category=current_category, is_available=True)
    else:
        products = Product.objects.filter(is_available=True)

    product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
        'categories': categories,
        'current_category': current_category,
        'current_subcategory': current_subcategory,
    }
    
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, subcategory_slug, product_slug):
    try:
        single_product = Product.objects.get(subcategory__slug=subcategory_slug, slug=product_slug)
    except Exception as e:
        raise e
    context = {
        'single_product': single_product,
    }
    return render(request, 'store/product_detail.html', context)


