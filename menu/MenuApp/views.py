from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import MenuItem, Category, Cuisine

# Create your views here.
def index(request):
    items = list(MenuItem.objects.values())
    return JsonResponse({'data': items})