from shop.models import Categories , SubCategory

def get_shop_context(request):
    categories =Categories.objects.all()
    context = {
        'categories':categories
    }

    return context
