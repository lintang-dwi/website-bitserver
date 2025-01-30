from django import forms
from .models import Product, Post

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'features', 'price', 'image']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [ 'title', 'content', 'image']
