from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField( null=True , blank=True)
    price = models.DecimalField(max_digits=10 , decimal_places=2 )
    image = models.ImageField(upload_to='photos/product_imgs/%y/%m/%d' , null=True , blank=True)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.
