from django.contrib import admin
from .models import MenuItem, Category, Cuisine, Ingredient

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(Cuisine)
admin.site.register(Ingredient)