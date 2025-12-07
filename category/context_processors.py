from .models import SubCategory, Category
def menu_links_subcategory(request):
    links = SubCategory.objects.all()
    
    return dict(links=links)

def menu_links_category(request):
    links = Category.objects.all()
    
    return dict(links=links)