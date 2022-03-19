from django.urls import path
from . import views


app_name = "assetsapp"
urlpatterns = [
    path('', views.index, name="index"),
    path('assets/', views.AssetView.as_view(), name="assets")
]
