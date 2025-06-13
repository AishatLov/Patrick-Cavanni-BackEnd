from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def home(request):
    return render(request, 'store/home.html')  # Main store page template

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['GET'])
def category_list(request):
    categories = Category.objects.filter(parent__isnull=True)  # Top-level categories
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    serializer = CategorySerializer(category)
    return Response(serializer.data)

@api_view(['GET'])
def cart_view(request):
    return render(request, 'store/cart.html')  # Cart page template

@api_view(['GET'])
def checkout_view(request):
    return render(request, 'store/checkout.html')  # Checkout page template