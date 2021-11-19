from django.db.models import fields
from rest_framework import serializers
from apps.inventory.models import Category,Product,Item
from drf_extra_fields.fields import Base64ImageField

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)
    class Meta:
        model = Item
        fields = '__all__'
        extra_kwargs = {'image': {'required': False},'description': {'required': False},'price': {'required': False},'product': {'required': False}} 