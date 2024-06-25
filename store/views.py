from django.shortcuts import render

from cart.models import Cart


def view_home(request):
    user = request.user
    count = 0
    if user.is_authenticated:
        count = Cart.objects.filter(user=user).count()
    return render(request, 'store/home.html', {'count': count})
