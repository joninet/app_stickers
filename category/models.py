from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=20, unique= True)
    description = models.CharField(max_length=255, blank = True)
    slug = models.CharField(max_length=100, unique = True)
    cat_image = models.ImageField(upload = 'photos/categories', blank = True)