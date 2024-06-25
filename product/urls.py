from django.urls import path

from product.views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView, CategoryListView, \
    CategoryCreateView, CategoryUpdateView, ProductDetailView, CategoryDetailView
from product.apps import ProductConfig

app_name = ProductConfig.name

urlpatterns = [
    # Category
    path('', CategoryListView.as_view(), name='category_home'),
    path('<slug>', CategoryDetailView.as_view(), name='category_view'),
    path('create/', CategoryCreateView.as_view(), name='category_create'),
    path('update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),

    # Product
    path('product/', ProductListView.as_view(), name='home'),
    path('<int:pk>/', ProductDetailView.as_view(), name='view'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),

]
