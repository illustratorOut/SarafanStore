from django import forms

from cart.models import Cart
from users.forms import StyleFormMixin


class CartForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Cart
        exclude = ('release_date', )

        # widgets = {
        #     'price': forms.NumberInput(
        #         attrs={
        #             'min': 1,
        #         }),
        # }
