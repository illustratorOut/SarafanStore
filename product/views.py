from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import paginator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.list import MultipleObjectMixin

from cart.models import Cart, CartProduct
from product.forms import ProductForm
from product.models import Product, Category, Subcategory


class ProductDetailView(DetailView):
    """Класс просмотра 1 продукта"""
    model = Product

    # paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.is_authenticated:
            context['count'] = Cart.objects.filter(user=user).count()
        category_pk = context.get('object').pk
        context['object_list'] = Product.objects.filter(subcategory=category_pk)
        context['subcategory'] = Subcategory.objects.filter(pk=category_pk).first()

        return context


class ProductListView(ListView):
    """Класс отображения продукта"""
    model = Product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        user = self.request.user

        if user.is_authenticated:
            context['count'] = CartProduct.objects.filter(user=user).count()

        search_query = self.request.GET.get('search_query')
        if search_query:
            res = Product.objects.filter(title__icontains=str(search_query).strip())
            context['object_list'] = res
            context['search_query'] = self.request.GET.get('search_query')
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


class CategoryDetailView(DetailView):
    """Класс просмотра 1 категории"""
    model = Category

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['Subcategory'] = Subcategory.objects.all()

        user = self.request.user
        if user.is_authenticated:
            context['count'] = CartProduct.objects.filter(user=user).count()

        category_slug = context.get('object').slug
        res = Subcategory.objects.filter(category__slug=category_slug)
        result = [Product.objects.filter(subcategory=item) for item in res if Product.objects.filter(subcategory=item)]
        context['object_list'] = result

        return context


class CategoryListView(ListView):
    """Класс отображения категории"""
    model = Category

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['Subcategory'] = Subcategory.objects.all()
        user = self.request.user

        if user.is_authenticated:
            context['count'] = CartProduct.objects.filter(user=user).count()

        search_query = self.request.GET.get('search_query')
        if search_query:
            res = Product.objects.filter(title__icontains=str(search_query).strip())
            context['object_list'] = res
            context['search_query'] = self.request.GET.get('search_query')

        return context


class CategoryCreateView(LoginRequiredMixin, CreateView):
    """Класс создания категории"""
    model = Category
    form_class = ProductForm
    success_url = reverse_lazy('store:home')

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    """Класс редактирования категории"""
    model = Category
    form_class = ProductForm
    success_url = reverse_lazy('store:home')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        return form


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    """Класс удаления категории"""
    model = Category
    success_url = reverse_lazy('store:home')



