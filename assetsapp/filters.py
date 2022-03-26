import django_filters
from django.db.models import CharField
from django.forms import CheckboxInput

from .models import Asset


class AssetFilter(django_filters.FilterSet):

    min_date = django_filters.DateFilter(
        field_name = 'purchase_date',
        lookup_expr = 'gte',
        label = 'Min. Purchase Date'
    )
    max_date = django_filters.DateFilter(
        field_name = 'purchase_date',
        lookup_expr = 'lte',
        label = 'Max. Purchase Date'
    )
    min_price = django_filters.NumberFilter(
        field_name = 'purchase_price',
        lookup_expr = 'gte',
        label = 'Min. Price'
    )
    max_price = django_filters.NumberFilter(
        field_name = 'purchase_price',
        lookup_expr = 'lte',
        label = 'Max. Price'
    )
    
    class Meta:
        model = Asset
        fields = ['name', 'current_status']
        #fields = {
        #    'name': ['icontains'],
        #    'purchase_price': ['lte', 'gte'],
        #    'purchase_date': ['lte', 'gte'],
        #    'current_status': ['in'],
        #}
