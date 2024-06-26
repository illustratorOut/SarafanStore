from django.urls import path

from cart.apps import CartConfig
from cart.view.API_cart import CartListAPIView, CartCreateAPIView, CartDeleteAPIView, CartUpdateAPIView, \
    CartCleanAPIView, CartInfoAPIView
from cart.view.cart import CartListView, product_add_cart, change_qty_cart, clean_cart, product_delete_cart

app_name = CartConfig.name

urlpatterns = [
    # Cart
    path('', CartListView.as_view(), name='home'),
    path('create/<int:pk>/', product_add_cart, name='product_add_cart'),
    path('change/<int:pk>/', change_qty_cart, name='change_qty_cart'),
    path('clean/', clean_cart, name='clean_cart'),
    path('delete/<int:pk>/', product_delete_cart, name='product_delete_cart'),

    # API Cart
    path('API/', CartListAPIView.as_view()),
    path('API/create/', CartCreateAPIView.as_view()),
    path('API/update/<int:pk>/', CartUpdateAPIView.as_view()),
    path('API/delete/<int:pk>/', CartDeleteAPIView.as_view()),

    path('API/clean/<int:pk>/', CartCleanAPIView.as_view()),
    path('API/info/', CartInfoAPIView.as_view()),

]
