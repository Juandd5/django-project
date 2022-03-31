from django.urls import path
from . import views


app_name = "assetsapp"
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('assets/', views.AssetView.as_view(), name="assets"),
    path('assets/<int:pk>', views.AssetDetail.as_view(), name="asset_detail"),
    path('assets/new/', views.AssetCreate.as_view(), name='asset_create'),
    path('assets/<int:pk>/update/', views.AssetUpdate.as_view(), name='asset_update'),
    path('persons/', views.PersonView.as_view(), name='persons'),
    path('persons/new/', views.PersonCreate.as_view(), name='person_create'),
    path('persons/<int:pk>/update/', views.PersonUpdate.as_view(), name='person_update'),
    path('persons/<int:pk>/delete/', views.PersonDelete.as_view(), name='person_delete'),
    path('areas/', views.AreaView.as_view(), name='areas'),
]
