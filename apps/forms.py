from django.forms import ModelForm

from apps.models import Product,Category,Tag


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ()

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        exclude = ()

class TagForm(ModelForm):
    class Meta:
        model = Tag
        exclude = ()
