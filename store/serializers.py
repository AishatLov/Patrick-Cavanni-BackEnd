from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all(), source='subcategories')

    class Meta:
        model = Category
        fields = ['id', 'name', 'parent', 'subcategories']

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Nested serializer for category

    class Meta:
        model = Product
        fields = '__all__'