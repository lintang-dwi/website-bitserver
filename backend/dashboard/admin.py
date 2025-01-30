from django.contrib import admin
from .models import Product, Post

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'description']
    search_fields = ['title', 'description']
    list_filter = ['price']

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    search_fields = ['title', 'content']
    list_filter = ['created_at']

admin.site.register(Product, ProductAdmin)
admin.site.register(Post, PostAdmin)
