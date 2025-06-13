from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category')  # Display these fields in the admin list view
    search_fields = ('name',)  # Add a search bar for product names
    list_filter = ('category',)  # Filter products by category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')  # Display category name and parent in the admin list view
    search_fields = ('name',)  # Add a search bar for category names

# Registering the models with the admin site
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)