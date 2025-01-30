from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, PostViewSet
from . import views


router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # API untuk produk dan post
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard

    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
]
