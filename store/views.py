from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from store.forms import ProductForm
from store.models import Category


class CategoryDetailView(DetailView):
    """Класс просмотра 1 категории"""
    model = Category


class CategoryListView(ListView):
    """Класс отображения категории"""
    model = Category

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
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
