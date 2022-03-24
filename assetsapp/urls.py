from django.urls import path
from . import views


app_name = "assetsapp"
urlpatterns = [
    path('', views.index, name="index"),
    path('assets/', views.assets_list_view, name="assets"),
    path('assets/<int:pk>', views.AssetDetail.as_view(), name="asset_detail"),
    path('assets/new/', views.AssetCreate.as_view(), name='create_asset'),
]
