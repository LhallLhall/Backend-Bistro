from django.urls import path
from . import views

urlpatterns = [
    path('cuisine_<str:cuisine>', views.filtered_cuisine),
    path('category_<str:category>', views.filtered_cat),
    path('', views.index, name='index'),
]