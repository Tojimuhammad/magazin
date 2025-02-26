from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(RootCategory)
admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(Phone)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)