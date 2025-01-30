from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, PostViewSet, api_root  # Tambahkan api_root
from . import views

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('api/', api_root, name='api-root'),  # ✅ API root diperbaiki
    path('api/', include(router.urls)),  # API endpoint untuk produk & post
    
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
]
