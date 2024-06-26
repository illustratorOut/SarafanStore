from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from product.models import Product, ProductImageInline
from product.validators import TitleValidator, PriceValidator, SubcategoryValidator


class ImageInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageInline
        fields = ('img',)


class ProductSerializer(serializers.ModelSerializer):
    imgs = ImageInlineSerializer(source='productimageinline_set', many=True, read_only=True)
    category = SerializerMethodField()
    subcategory = SerializerMethodField()

    class Meta:
        model = Product
        fields = ('category', 'subcategory', 'title', 'slug', 'price', 'img', 'imgs')

    def get_category(self, instance):
        return str(instance.subcategory.category.title)

    def get_subcategory(self, instance):
        if instance.subcategory.title:
            return str(instance.subcategory.title)


class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        validators = [
            TitleValidator(field='title'),
            PriceValidator(field='price'),
            SubcategoryValidator(field='subcategory'),
        ]
