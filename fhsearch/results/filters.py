import django_filters
from django_filters import NumberFilter, CharFilter

from .models import *

class StatsFilter(django_filters.FilterSet):
    points = NumberFilter()
    points_gt = NumberFilter(field_name='points', lookup_expr='gt')
    points_lt = NumberFilter(field_name='points', lookup_expr='lt')
    player = CharFilter(field_name='player', lookup_expr='icontains')
    class Meta:
        model = Stats
        fields = '__all__'
        exclude = ['player']
