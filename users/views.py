from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from cart.models import Cart
from users.forms import UserProfileForm, UserRegisterForm
from users.models import User


class RegisterView(CreateView):
    """Регистрация пользователя"""
    model = User
    form_class = UserRegisterForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('users:login')


class ProfileView(UpdateView):
    """Профиль пользователя"""
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.is_authenticated:
            context['count'] = Cart.objects.filter(user=user).count()
        return context
