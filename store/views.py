from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category, SubCategory 
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

def store(request, category_slug=None, subcategory_slug=None):
    categories = Category.objects.all()
    current_category = None
    current_subcategory = None
    
    if subcategory_slug:
        current_subcategory = get_object_or_404(SubCategory, slug=subcategory_slug)
        current_category = current_subcategory.category
        products = Product.objects.filter(subcategory=current_subcategory, is_available=True).order_by('id')
        
        paginator = Paginator(products, 2)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    elif category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        # Filtrar productos que tengan subcategorías de esta categoría
        products = Product.objects.filter(subcategory__category=current_category, is_available=True).order_by('id')
        
        paginator = Paginator(products, 2)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.filter(is_available=True).order_by('id')
        paginator = Paginator(products, 2)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        
        product_count = products.count()

    context = {
        'products': paged_products,
        'product_count': product_count,
        'categories': categories,
        'current_category': current_category,
        'current_subcategory': current_subcategory,
    }
    
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, subcategory_slug, product_slug):
    try:
        single_product = Product.objects.get(subcategory__slug=subcategory_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e
    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    return render(request, 'store/product_detail.html', context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-create_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            product_count = products.count()
            print(products)
            
    context = {
        'products': products,
        'product_count': product_count,
    }
    
    return render(request, 'store/store.html', context)
            
            