from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView

from cart.models import CartProduct, Cart
from product.models import Product


class CartListView(LoginRequiredMixin, ListView):
    """Класс отображения корзины"""
    model = CartProduct

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.is_authenticated:
            context['all_count'] = sum([item.quantity for item in CartProduct.objects.filter(user=user)])
            context['count'] = CartProduct.objects.filter(user=user).count()
            context['all_price'] = sum(
                [item.product.price * item.quantity for item in CartProduct.objects.filter(user=user)])
            context['object_list'] = CartProduct.objects.filter(user=user)

        return context


def product_add_cart(request, pk):
    '''Добавить продукт в корзину(создать)'''
    product = Product.objects.get(pk=pk)
    user = request.user
    if user.is_authenticated:
        cart = Cart.objects.filter(user=user).first()
        cart_product = CartProduct.objects.filter(user=user, product=product)

        if not cart:
            cart = Cart.objects.create(user=user)
        if cart_product:
            res = CartProduct.objects.filter(user=user, product=product).first()
            res.quantity += 1
            res.save()
        else:
            CartProduct.objects.get_or_create(user=user, cart=cart, product=product, quantity=1)
    return redirect('cart:home')


def product_delete_cart(request, pk):
    '''Удалить продукт из корзины'''
    product = Product.objects.get(pk=pk)
    user = request.user
    if user.is_authenticated:
        CartProduct.objects.get(user=user, product=product).delete()
    return redirect('cart:home')


def clean_cart(request):
    '''Очистить корзину'''
    user = request.user
    if user.is_authenticated:
        CartProduct.objects.filter(user=user).delete()
    return redirect('cart:home')


def change_qty_cart(request, pk):
    """Изменить кол-во продуктов в корзине"""
    product = Product.objects.get(pk=pk)
    user = request.user

    if user.is_authenticated:
        if CartProduct.objects.filter(user=user, product=product).first().quantity != 1:
            res = CartProduct.objects.filter(user=user, product=product).first()
            res.quantity -= 1
            res.save()
        else:
            CartProduct.objects.get(user=user, product=product).delete()
    return redirect('cart:home')
