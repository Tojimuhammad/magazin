from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import PhoneSerializer
from. models import Phone
from django_filters.rest_framework import DjangoFilterBackend

class PhoneView(ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class  = PhoneSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']