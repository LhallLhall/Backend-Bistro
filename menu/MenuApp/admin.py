from django.contrib import admin
from .models import MenuItem
from .models import Category
from .models import Cuisine

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(Cuisine)