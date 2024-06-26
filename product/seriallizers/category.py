from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from product.models import Category, Subcategory


class CommentSerializer:
    pass


class CategorySerializer(serializers.ModelSerializer):
    subcategory = SerializerMethodField()

    class Meta:
        model = Category
        fields = ['title', 'slug', 'img', 'subcategory']

    def get_subcategory(self, instance):
        category_pk = instance.pk
        subcategory = Subcategory.objects.filter(category=category_pk)
        res = [f'{item.title} slug:({item.slug})' for item in subcategory if item.category]
        return res
