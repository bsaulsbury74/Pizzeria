from django.db import models
from Pizzeria.settings import TIME_ZONE
from django.db.models import Model
# Create your models here.

class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)


    def __str__(self):
        return self.pizza_name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    toppingname = models.CharField(max_length=100)
    

    def __str__(self):
        return self.toppingname

class Comment(models.Model):
    pizza= models.ForeignKey(Pizza, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    date_added= models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.comment

class Picture(Model):
    pizza= models.ForeignKey(Pizza, on_delete=models.CASCADE)
    picture= models.ImageField(upload_to='upload/')
    

