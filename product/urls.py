from django.urls import path

from product.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from product.apps import ProductConfig

app_name = ProductConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('view/<int:pk>', ProductDetailView.as_view(), name='view'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),

]
