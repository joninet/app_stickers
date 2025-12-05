from django.contrib import admin

from .models import Product
from category.models import Category


class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name', 'price', 'stock', 'subcategory', 'get_category', 'modified_date', 'is_available')
    readonly_fields = ('product_code',)
    prepopulated_fields = {'slug': ('product_name',)}
    
    def get_category(self, obj):
        return obj.subcategory.category  # accede a la categoría
    get_category.short_description = 'Categoría'  # nombre en el admin
    
admin.site.register(Product, ProductAdmin)