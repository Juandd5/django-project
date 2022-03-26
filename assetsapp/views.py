from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Asset
from .forms import AssetCreateForm, AssetUpdateForm
from .filters import AssetFilter


def index(request):
    return render(request, 'assetsapp/index.html')


class ModelView(View):
    model = Asset


class AssetFilterView(ModelView, ListView):
    template_name = 'assetsapp/asset.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        assets = self.get_queryset()
        filter = AssetFilter(self.request.GET, queryset=assets)
        context['filter'] = filter
        return context


class AssetDetail(ModelView, DetailView):
    template_name = 'assetsapp/asset_detail.html'


class AssetBaseView(ModelView, View):
    template_name = 'assetsapp/asset_form.html'
    success_url = reverse_lazy('assetsapp:assets')


class AssetCreate(AssetBaseView, CreateView):
    form_class = AssetCreateForm


class AssetUpdate(AssetBaseView, UpdateView):
    form_class = AssetUpdateForm
