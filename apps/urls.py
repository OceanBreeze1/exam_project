from django.urls import path

from apps.views import home, get_laptops, product_detail

urlpatterns = [
    path('', home, name='home'),
    path('get_laptops/<int:pk>', get_laptops, name='get_laptops'),
    path('product_detail/<int:pk>',product_detail,name='product_detail')
]
