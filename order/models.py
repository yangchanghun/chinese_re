from django.db import models
from seller.models import Food
from django.contrib.auth.models import User

# Create your models here.
# class Category(models.Model):
#     name = models.CharField(max_length=200)
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    food = models.ForeignKey(Food,on_delete=models.DO_NOTHING)
    amount = models.IntegerField(default=0)