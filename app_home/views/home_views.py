from django.shortcuts import render
from store.models import Product
import random

# Create your views here.
def home(request):
    products = Product.objects.filter(is_available=True)

    gradients = [
        "from-red-400 to-pink-500",
        "from-blue-400 to-purple-500",
        "from-green-400 to-emerald-500",
        "from-yellow-400 to-orange-500",
        "from-indigo-400 to-blue-500",
        "from-purple-400 to-fuchsia-500",
        "from-pink-400 to-rose-500",
        "from-red-400 to-yellow-500",
    ]

    # Agrego una clase random a cada producto
    for p in products:
        p.color_class = random.choice(gradients)

    context = {
        'products': products
    }
    return render(request, 'home.html', context)