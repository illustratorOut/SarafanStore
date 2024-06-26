from rest_framework.generics import DestroyAPIView, ListAPIView, UpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from cart.models import CartProduct, Cart
from cart.seriallizers.cart import CartUpdateSerializer, CartCreateSerializer, CartCleanSerializer, CartInfoSerializer
from product.paginators import CustomPagination
from product.permissions import IsOwner


class CartListAPIView(ListAPIView):
    '''API Отображение списка продуктов'''
    queryset = CartProduct.objects.all()
    serializer_class = CartCreateSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = CustomPagination


class CartCreateAPIView(CreateAPIView):
    '''API Создание продукта'''
    queryset = CartProduct.objects.all()
    serializer_class = CartCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        '''При создании продукта присваиваем автора(user)'''
        product = serializer.save()
        product.user = self.request.user
        product.save()


class CartUpdateAPIView(UpdateAPIView):
    '''API Редактирование (обновление) продукта'''
    queryset = CartProduct.objects.all()
    serializer_class = CartUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class CartDeleteAPIView(DestroyAPIView):
    '''API Удаление продукта'''
    queryset = CartProduct.objects.all()
    serializer_class = CartCreateSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class CartCleanAPIView(DestroyAPIView):
    '''API Очистить корзину'''
    queryset = Cart.objects.all()
    serializer_class = CartCleanSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = CustomPagination


class CartInfoAPIView(ListAPIView):
    '''API Информация о корзине'''
    queryset = Cart.objects.all()
    serializer_class = CartInfoSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        cart = Cart.objects.filter(user=user)
        if cart:
            queryset = cart
        return queryset
