from django.db import models

from category.models import SubCategory
# Create your models here.

class Product(models.Model):
    product_code = models.CharField(max_length=10, unique=True, blank=True)

    product_name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, unique=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)

    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Solo generar si el producto es nuevo y no tiene código
        if not self.product_code:
            prefix = self.subcategory.subcategory_name[:3].upper()

            # Buscar el último código que empieza con ese prefijo
            last_product = Product.objects.filter(
                subcategory=self.subcategory,
                product_code__startswith=prefix
            ).order_by('-product_code').first()

            if last_product:
                last_number = int(last_product.product_code[3:])
                new_number = last_number + 1
            else:
                new_number = 1

            number_str = str(new_number).zfill(3)  # 001, 002, etc.

            generated_code = f"{prefix}{number_str}"

            # Verificar que sea único
            while Product.objects.filter(product_code=generated_code).exists():
                new_number += 1
                number_str = str(new_number).zfill(3)
                generated_code = f"{prefix}{number_str}"

            self.product_code = generated_code

        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name

    
    