from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Area, Asset, Person
from .forms import AssetCreateForm, AssetUpdateForm, PersonForm
from .filters import AssetFilter


class IndexView(TemplateView):
    template_name = 'assetsapp/index.html'


# Asset Views

class BaseModelAssetviews(View):
    model = Asset


class AssetView(BaseModelAssetviews, ListView):
    template_name = 'assetsapp/asset.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        assets = self.get_queryset()
        filter = AssetFilter(self.request.GET, queryset=assets)
        context['filter'] = filter
        return context


class AssetDetail(BaseModelAssetviews, DetailView):
    template_name = 'assetsapp/asset_detail.html'


class AssetBaseView(BaseModelAssetviews):
    template_name = 'assetsapp/asset_form.html'
    success_url = reverse_lazy('assetsapp:assets')


class AssetCreate(AssetBaseView, CreateView):
    form_class = AssetCreateForm


class AssetUpdate(AssetBaseView, UpdateView):
    form_class = AssetUpdateForm


# Person Views

class BaseModelPersonViews(View):
    model = Person


class PersonView(BaseModelPersonViews, ListView):
    template_name = 'assetsapp/person.html'
    context_object_name = 'persons'


class PersonBaseView(BaseModelPersonViews):
    template_name = 'assetsapp/person_form.html'
    success_url = reverse_lazy('assetsapp:persons')
    form_class = PersonForm


class PersonCreate(PersonBaseView, CreateView):
    pass


class PersonUpdate(PersonBaseView, UpdateView):
    pass


class PersonDelete(BaseModelPersonViews, DeleteView):
    template_name = "assetsapp/person_delete.html"
    success_url = reverse_lazy('assetsapp:persons')


# Area Views

class AreaView(ListView):
    model = Area
    template_name = 'assetsapp/area.html'
    context_object_name = 'areas'
