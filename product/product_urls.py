from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path('product/', views.product, name='product'),
    path("<slug:name_model_slug>/", views.product, name="product_model"),
    path("product/<slug:category_slug>/", views.product, name="product_category"),
    path('product_item/', views.product_item, name='product_item'),
    path("product_item/<slug:slug>/", views.product_item, name="product_item")
]
