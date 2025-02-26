from rest_framework.serializers import ModelSerializer
from .models import *
from users.serializers import UserSerializer

class RootCategorySerializer(ModelSerializer):
    class Meta:
        model = RootCategory
        fields = '__all__'
        

class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PhoneSerializer(ModelSerializer):
    # category = CategorySerializer()
    class Meta:
        model = Phone
        # fields = ['name']
        fields = ['id','name', 'category','info', 'ddr', 'storage', 'color', 'display', 'camera', 'battery', 'price', 'discount', 'is_week_product']
        # depth = 3


class CartSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    product = PhoneSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(ModelSerializer):
    order = OrderSerializer(read_only=True)
    product = PhoneSerializer(read_only=True)
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'order', 'quantity', 'price']