from django.urls import path
from store.apps import StoreConfig
from store.views import CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView

app_name = StoreConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),

    path('catalog', CategoryListView.as_view(), name='catalog_home'),
    path('catalog/<slug>', CategoryDetailView.as_view(), name='view'),
    path('create/', CategoryCreateView.as_view(), name='create'),
    path('update/<int:pk>/', CategoryUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CategoryDeleteView.as_view(), name='delete'),

]
