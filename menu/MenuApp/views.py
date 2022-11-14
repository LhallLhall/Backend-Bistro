from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import MenuItem, Category, Cuisine, Ingredient
from django.forms.models import model_to_dict

# Create your views here.
def index(request):
    item_list = []
    items = MenuItem.objects.all()
    
    for item in items:
        cat_model_instance = Category.objects.get(id=item.category_id)
        cuisine_model_instance = Cuisine.objects.get(id=item.cuisine_id)
        
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
            },
            'ingredients': ''.join(str(list(item.ingredients.values_list('ingredient')))),
            # join([str(x) for x in Ingredient.objects.get(pk=ingredient_id).ingredient.all()])
            
        })
    return JsonResponse({'data': item_list})
    #
def filtered_cat(request, category):
    filtered_list = list(MenuItem.objects.filter(category__title=category).values())
    
    if len(filtered_list) >= 1:
        return JsonResponse({'data': filtered_list})
    else:
        return HttpResponse('Error: There were no items in '+category)
    return JsonResponse({'data': filtered_list})

def filtered_cuisine(request, cuisine):
    filtered_list = list(MenuItem.objects.filter(cuisine__title=cuisine).values())
    if len(filtered_list) >= 1:
        return JsonResponse({'data': filtered_list})
    else:
        return HttpResponse('Error: There were no items in '+ category)