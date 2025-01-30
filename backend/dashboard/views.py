from rest_framework import viewsets
from .models import Product, Post
from .serializers import ProductSerializer, PostSerializer
from django.shortcuts import render, redirect
from .forms import ProductForm, PostForm

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Post
from .forms import ProductForm, PostForm


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


## View untuk dashboard
def dashboard(request):
    products = Product.objects.all()  # Mengambil semua produk
    posts = Post.objects.all()  # Mengambil semua post

    if request.method == 'POST':
        if 'submit_product' in request.POST:
            product_form = ProductForm(request.POST, request.FILES)
            if product_form.is_valid():
                product_form.save()
                return redirect('dashboard')
        elif 'submit_post' in request.POST:
            post_form = PostForm(request.POST, request.FILES)
            if post_form.is_valid():
                post_form.save()
                return redirect('dashboard')
    else:
        product_form = ProductForm()
        post_form = PostForm()

    return render(request, 'dashboard/dashboard.html', {
        'product_form': product_form,
        'post_form': post_form,
        'products': products,
        'posts': posts,
    })

# Edit Product
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES, instance=product)
        if product_form.is_valid():
            product_form.save()
            return redirect('dashboard')
    else:
        product_form = ProductForm(instance=product)

    return render(request, 'dashboard/edit_product.html', {'product_form': product_form, 'product': product})

# Edit Post
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('dashboard')
    else:
        post_form = PostForm(instance=post)

    return render(request, 'dashboard/edit_post.html', {'post_form': post_form, 'post': post})

# Delete Product
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('dashboard')

# Delete Post
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('dashboard')