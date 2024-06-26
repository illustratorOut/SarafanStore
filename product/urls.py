from django.urls import path

from product.view.API_product import ProductListAPIView, ProductDetailAPIView, ProductCreateAPIView, \
    ProductUpdateAPIView, ProductDeleteAPIView, CategoryListAPIView
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

    # API Product
    path('API/', ProductListAPIView.as_view()),
    path('API/<int:pk>/', ProductDetailAPIView.as_view()),
    path('API/create/', ProductCreateAPIView.as_view()),
    path('API/update/<int:pk>/', ProductUpdateAPIView.as_view()),
    path('API/delete/<int:pk>/', ProductDeleteAPIView.as_view()),

    # API Category
    path('API/category/', CategoryListAPIView.as_view()),

]
