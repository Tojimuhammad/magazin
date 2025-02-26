from django_filters import rest_framework as filters
from shop.models import Phone

class PhoneFilter(filters.FilterSet):

    class Meta:
        model = Phone
        fields = '__all__'