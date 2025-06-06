from rest_framework import serializers
from product.models import Product
from product.serializers.category_serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=True, many=True)

    class Meta:
        model = Product
        fields = ['titel', 'description', 'price', 'active', 'category']