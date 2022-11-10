from django.db import models

# Create your models here.
class MenuItem(models.Model):
    title = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=200)
    price = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    spicy_level = models.IntegerField(null=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE,)
    cuisine = models.ForeignKey("Cuisine", on_delete=models.CASCADE,)
    def __str__(self):
        return self.title + ' : ' + str(self.price) + '$'

class Category(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Cuisine(models.Model):
    title = models.CharField(max_length=200)
    def __str__(self):
        return self.title