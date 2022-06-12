from dataclasses import fields
import django_filters
from django_filters import DateFilter
from .models import RegistrationModel

class RegistrationFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date',lookup_expr='gte')
    end_date = DateFilter(field_name='date',lookup_expr='lte')
    class Meta:
        model=RegistrationModel
        fields=['email','mobile','date']
        exclude=['date','date']
