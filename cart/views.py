from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from cart.forms import CartForm
from cart.models import Cart
from product.models import Product


class CartDetailView(DetailView):
    """Класс просмотра 1 корзины"""
    model = Cart


class CartListView(LoginRequiredMixin, ListView):
    """Класс отображения корзины"""
    model = Cart

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.is_authenticated:
            context['all_count'] = sum([item.quantity for item in Cart.objects.filter(user=user)])
            context['count'] = Cart.objects.filter(user=user).count()
            context['all_price'] = sum([item.product.price * item.quantity for item in Cart.objects.filter(user=user)])
            context['object_list'] = Cart.objects.filter(user=user)

        return context


class CartCreateView(LoginRequiredMixin, CreateView):
    """Класс создания корзины"""
    model = Cart
    form_class = CartForm
    success_url = reverse_lazy('product:home')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class CartUpdateView(LoginRequiredMixin, UpdateView):
    """Класс редактирования корзины"""
    model = Cart
    form_class = CartForm
    success_url = reverse_lazy('product:home')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        return form


class CartDeleteView(LoginRequiredMixin, DeleteView):
    """Класс удаления корзины"""
    model = Cart
    success_url = reverse_lazy('cart:home')


def add_to_cart(request, pk):
    product = Product.objects.get(pk=pk)
    user = request.user

    if Cart.objects.filter(user=user, product=product):
        res = Cart.objects.filter(user=user, product=product)[0]
        a = res.quantity + 1
        Cart.objects.filter(user=user, product=product).update(quantity=a)
    else:
        cart, _ = Cart.objects.get_or_create(user=user, product=product, quantity=1)

    return redirect('cart:home')


def delete_quantity_to_cart(request, pk):
    product = Product.objects.get(pk=pk)
    user = request.user

    if Cart.objects.filter(user=user, product=product).first().quantity != 1:
        res = Cart.objects.filter(user=user, product=product)[0]
        a = res.quantity - 1
        Cart.objects.filter(user=user, product=product).update(quantity=a)
    else:
        Cart.objects.get(user=user, product=product).delete()

    return redirect('cart:home')


def delete_to_cart(request, pk):
    product = Product.objects.get(pk=pk)
    user = request.user
    Cart.objects.get(user=user, product=product).delete()
    return redirect('cart:home')


def all_delete_to_cart(request):
    user = request.user
    Cart.objects.filter(user=user).delete()
    return redirect('cart:home')
