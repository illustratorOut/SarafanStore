from django import forms

from cart.models import CartProduct
from users.forms import StyleFormMixin


class CartForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = CartProduct
        exclude = ('release_date', )
