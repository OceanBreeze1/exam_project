from django.shortcuts import render

from apps.models import Product


def home(request):
    return render(request, 'limupa-digital-products-store-ecommerce/index.html')


def get_laptops(request, pk):
    products = Product.objects.filter(category_id=pk)
    context = {'products': products,
               'count': products.count()}
    return render(request, 'limupa-digital-products-store-ecommerce/blog-list-left-sidebar.html', context)


def product_detail(request,pk):
    products = Product.objects.filter(id=pk)
    context = {'products': products}
    return render(request, 'limupa-digital-products-store-ecommerce/blog-details-left-sidebar.html', context)
