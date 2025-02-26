from django.db import models
from users.models import User
# Create your models here.
class RootCategory(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    root_category = models.ForeignKey(RootCategory, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Phone(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    info = models.TextField()
    ddr = models.CharField(max_length=255)
    storage = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    display = models.CharField(max_length=255)
    camera = models.CharField(max_length=255)
    battery = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    is_week_product = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Cart(models.Model):
    product = models.ForeignKey(Phone, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.PositiveIntegerField()
    address = models.CharField(max_length = 255)
    status = models.IntegerField(choices=[
        (1, 'joylandi'),
        (2, 'tayyorlanmoqda'),
        (3, 'yuborildi'),
        (4, 'yetkazildi')
    ], default=1)


class OrderItem(models.Model):
    product = models.ForeignKey(Phone, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()