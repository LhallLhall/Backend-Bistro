from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import MenuItem, Category, Cuisine
from django.forms.models import model_to_dict

# Create your views here.
def index(request):
    item_list = []
    items = MenuItem.objects.all()
    for item in items:
        cat_model_instance = Category.objects.get(id=item.category_id)
        cuisine_model_instance = Cuisine.objects.get(id=item.category_id)
        item_list.append({
            'title': item.title,
            'description': item.description,
            'price': item.price,
            'spicy level': item.spicy_level,
            'category': {
                'id': cat_model_instance.id,
                'title': cat_model_instance.title,
            },
            'cuisine': {
                'id': cuisine_model_instance.id,
                'title': cuisine_model_instance.title,
            }
        })

    return JsonResponse({'data': item_list})
    # 