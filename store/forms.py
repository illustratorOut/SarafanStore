from django import forms
from store.models import Product
from users.forms import StyleFormMixin


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('release_date', 'author',)

        widgets = {
            'price': forms.NumberInput(
                attrs={
                    'min': 1,
                }),
        }
