from django.db import models

class Product(models.Model):
    image = models.ImageField(upload_to='users/',blank=True,null=True)
    product_name= models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    pruduct_data = models.CharField(max_length=255)
    category = models.ForeignKey('apps.Category', models.CASCADE)


    def __str__(self):
        return self.product_name

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.name

# Create your models here.
