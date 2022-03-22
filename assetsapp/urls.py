from django.urls import path
from . import views


app_name = "assetsapp"
urlpatterns = [
    path('', views.index, name="index"),
    path('assets/', views.assets_list_view, name="assets")
]
