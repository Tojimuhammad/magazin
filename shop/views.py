from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import *
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET'])
def root_category(request):
    r_cats = RootCategory.objects.all()
    ser = RootCategorySerializer(r_cats, many=True)
    return Response(ser.data)

@api_view(['GET'])
def sub_category(request):
    s_cats = SubCategory.objects.all()
    ser = SubCategorySerializer(s_cats, many=True)
    return Response(ser.data)

@api_view(['GET'])
def category(request):
    cats = Category.objects.all()
    ser = CategorySerializer(cats, many=True)
    return Response(ser.data)


@api_view(['GET'])
def phone_view(request):
    phones = Phone.objects.all()
    category = request.GET.get('category')
    name = request.GET.get('name')
    if category:
        phones = Phone.objects.filter(category_id=category)
    if name:
        phones = Phone.objects.filter(name = name)
    ser = PhoneSerializer(phones, many=True)
    return Response(ser.data)

from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PhoneFilter

class PhoneList(generics.ListAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['name', 'category', 'color', 'ddr']#'__all__'
    # filterset_fields = PhoneFilter

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_cart_view(request, pk):
    user = request.user
    product = Phone.objects.get(id=pk)
    quantity = request.POST.get('quantity')
    Cart.objects.create(
        user = user,
        product = product,
        quantity = quantity
    )
    return Response('Success')


@api_view(['GET'])
def cart_view(request):
    carts = Cart.objects.filter(user=request.user)
    ser = CartSerializer(carts, many=True)
    return Response(ser.data)


# @api_view(['GET'])
# def order_view(request):
#     orders = Order.objects.filter(user=request.user)
#     ser = OrderSerializer(orders, many=True)
#     return Response(ser.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order_view(request):
    user = request.user
    total = 0
    address = request.POST.get('address')
    order = Order.objects.create(user=user, total=total, address=address)
    carts = Cart.objects.filter(user=user)
    for item in carts:
        OrderItem.objects.create(
            product_id = item.product_id,
            order = order,
            quantity = item.quantity,
            price = item.product.price
            )
        order.total += item.quantity * item.product.price
        order.save()
    Cart.objects.filter(user=user).delete()
    return Response(OrderSerializer(order).data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_order_items(request, pk):
    order = Order.objects.get(id=pk)
    user = request.user
    items = OrderItem.objects.filter(order_id=order)
    return Response(OrderItemSerializer(items, many=True).data)