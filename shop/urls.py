from django.urls import path, include
from .views import *
from .viewTwo import PhoneView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'phone', PhoneView, basename='phone')

urlpatterns = [
    path('rootcategory/',root_category),
    path('subcategory/',sub_category),
    path('category/',category),
    path('phones/',phone_view),
    path('', include(router.urls)),
    path('telefonlar/', PhoneList.as_view()),
    path('cart/',cart_view),
    path('cart-create/<int:pk>/',create_cart_view),
    path('get-order-items/<int:pk>/', get_order_items),
    path('order-create/',create_order_view),
]