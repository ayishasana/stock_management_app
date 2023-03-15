from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_customer=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)

class register(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=10,null=False)
    email = models.EmailField()

    def __str__(self):
        return self.name

class stock(models.Model):
    name = models.CharField(max_length=20)
    stock_id=models.IntegerField()
    product = models.CharField(max_length=50)
    price = models.IntegerField()
    quantity = models.IntegerField()