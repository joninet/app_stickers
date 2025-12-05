from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=20, unique= True)
    description = models.CharField(max_length=255, blank = True)
    slug = models.CharField(max_length=100, unique = True)
    cat_image = models.ImageField(upload_to = 'photos/categories', blank = True)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.category_name
    
class SubCategory(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategories'
    )
    subcategory_name = models.CharField(max_length=20)
    description = models.CharField(max_length=255, blank=True)
    slug = models.CharField(max_length=100, unique=True)
    subcat_image = models.ImageField(upload_to='photos/subcategories', blank=True)

    class Meta:
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'

    def __str__(self):
        return f"{self.category.category_name} - {self.subcategory_name}"
