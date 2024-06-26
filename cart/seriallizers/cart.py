from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from cart.models import CartProduct, Cart
from product.models import Product
from users.models import User


class ProductInCartSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['pk']


class CartProductSerializer(serializers.ModelSerializer):
    product = ProductInCartSerializer2(read_only=True)
    quantity = serializers.IntegerField()

    class Meta:
        model = CartProduct
        fields = ['product', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    cartproduct = CartProductSerializer(many=True, read_only=True)
    total = serializers.SerializerMethodField()

    def get_total(self, obj):
        total = 0
        for bp in obj.cartproduct.all():
            total += bp.product.price * bp.quantity
        return {"total": total}

    class Meta:
        model = Cart
        fields = ('pk',)


class CartUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = ('quantity',)


class CartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = '__all__'

    def create(self, validated_data):
        user = validated_data['user']
        new_cart = Cart.objects.filter(user=user).first()
        if not new_cart:
            Cart.objects.create(user=user)
            CartProduct.objects.create(**validated_data)
        else:
            CartProduct.objects.create(**validated_data)
        return CartProduct.objects.filter(user=user).first()


class CartCleanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = '__all__'


class CartInfoSerializer(serializers.ModelSerializer):
    total = SerializerMethodField()
    count = SerializerMethodField()
    product = SerializerMethodField()

    def get_total(self, obj):
        total = 0
        user = self.context['request'].user.pk

        for item in CartProduct.objects.filter(user=user):
            total += item.product.price * item.quantity
        return total

    def get_count(self, obj):
        count = 0
        user = self.context['request'].user.pk

        for item in CartProduct.objects.filter(user=user):
            count += item.quantity
        return count

    def get_product(self, obj):
        product = []
        user = self.context['request'].user.pk

        for item in CartProduct.objects.filter(user=user):
            product.append({'product': item.product.title, 'price':item.product.price, 'quantity':item.quantity})
        return product

    class Meta:
        model = CartProduct
        fields = ('product', 'count', 'total',)
