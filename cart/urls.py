from django.urls import path

from cart.apps import CartConfig
from cart.views import CartListView, CartDetailView, CartCreateView, CartUpdateView, CartDeleteView, add_to_cart, \
    delete_to_cart, all_delete_to_cart, delete_quantity_to_cart

app_name = CartConfig.name

urlpatterns = [
    # CART
    path('', CartListView.as_view(), name='home'),
    path('view/<int:pk>/', CartDetailView.as_view(), name='view'),
    path('create/', CartCreateView.as_view(), name='create'),
    path('update/<int:pk>/', CartUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CartDeleteView.as_view(), name='delete'),

    path('<int:pk>/', add_to_cart, name='add_to_cart'),
    path('delete_quantity_to_cart/<int:pk>/', delete_quantity_to_cart, name='delete_quantity_to_cart'),
    path('d/<int:pk>/', delete_to_cart, name='delite_to_cart'),
    path('del/', all_delete_to_cart, name='all_delite_to_cart'),
]
