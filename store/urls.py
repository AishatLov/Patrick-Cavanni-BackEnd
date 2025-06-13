from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('', views.home, name='store-home'),  # Main store page
    path('products/', views.product_list, name='product-list'),  # List of products
    path('products/<int:id>/', views.product_detail, name='product-detail'),  # Product details
    path('cart/', views.cart_view, name='cart'),  # Shopping cart
    path('checkout/', views.checkout_view, name='checkout'),  # Checkout page
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),  # OpenAPI schema
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Swagger UI
]