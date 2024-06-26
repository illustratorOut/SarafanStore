from rest_framework.generics import RetrieveAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from product.models import Product, Category
from product.paginators import CustomPagination
from product.permissions import IsOwner
from product.seriallizers.category import CategorySerializer
from product.seriallizers.product import ProductSerializer, ProductCreateSerializer


class CategoryListAPIView(ListAPIView):
    '''API Отображение списка категорий'''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
    pagination_class = CustomPagination


class ProductDetailAPIView(RetrieveAPIView):
    '''API Отображение продукта'''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class ProductListAPIView(ListAPIView):
    '''API Отображение списка продуктов'''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    pagination_class = CustomPagination


class ProductCreateAPIView(CreateAPIView):
    '''API Создание продукта'''
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        '''При создании продукта присваиваем автора(user)'''
        product = serializer.save()
        product.user = self.request.user
        product.save()


class ProductUpdateAPIView(UpdateAPIView):
    '''API Редактирование (обновление) продукта'''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class ProductDeleteAPIView(DestroyAPIView):
    '''API Удаление продукта'''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsOwner]
