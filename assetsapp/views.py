from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.views.generic.list import ListView

from .models import Asset


def index(request):
    return render(request, 'assetsapp/index.html')


def is_valid_queryparameter(parameter):
    return parameter != '' and parameter is not None


def filtering(request):
    query_set = Asset.objects.all()
    status_option = ['available', 'retired', 'under_repair', 'assigned']

    name = request.GET.get('name')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    min_purchase_date = request.GET.get('min_date')
    max_purchase_date = request.GET.get('max_date')
    valid_status_options = [
        request.GET.get(option)
        for option in status_option
        if is_valid_queryparameter(request.GET.get(option))
    ]

    if is_valid_queryparameter(name):
        query_set = query_set.filter(name__icontains=name)
    
    if is_valid_queryparameter(min_price):
        query_set = query_set.filter(purchase_price__gte=min_price)
    
    if is_valid_queryparameter(max_price):
        query_set = query_set.filter(purchase_price__lte=max_price)

    if is_valid_queryparameter(min_purchase_date):
        query_set = query_set.filter(purchase_date__gte=min_purchase_date)

    if is_valid_queryparameter(max_purchase_date):
        query_set = query_set.filter(purchase_date__lte=max_purchase_date)

    if valid_status_options:
        query_set = query_set.filter(current_status__in=(valid_status_options))

    return query_set


def assets_list_view(request):
    query_set = filtering(request)
    context = {
        'assets_list': query_set,
    }
    return render(request, 'assetsapp/assets.html', context)
