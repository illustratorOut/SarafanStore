from django import forms
from store.models import Category
from users.forms import StyleFormMixin


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('release_date', 'author',)
