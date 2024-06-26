from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    '''Являетсяли user создателем obj'''

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user:
            return True
        return False


class IsOwnerCartProduct(BasePermission):
    '''Являетсяли user создателем корзины'''

    def has_object_permission(self, request, view, obj):
        return obj.cart.user == request.user
