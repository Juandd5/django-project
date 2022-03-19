from django.shortcuts import render
from django.views.generic import ListView

from .models import Asset


def index(request):
    return render(request, 'assetsapp/index.html')


class AssetView(ListView):
    template_name = 'assetsapp/assets.html'
    context_object_name = 'assets_list'

    def get_queryset(self):
        return Asset.objects.all()

