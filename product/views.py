from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from product.models import Product
from store.forms import ProductForm


class ProductDetailView(DetailView):
    """Класс просмотра 1 продукта"""
    model = Product


class ProductListView(ListView):
    """Класс отображения продукта"""
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Класс создания продукта"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product:home')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Класс редактирования продукта"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product:home')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        return form


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """Класс удаления продукта"""
    model = Product
    success_url = reverse_lazy('product:home')
