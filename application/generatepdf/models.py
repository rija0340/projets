from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class Auteur (models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    pdp = models.ImageField()

    def __str__(self):
        return self.user.username


class Products(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(default=0.00, max_digits=18, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "tutorial_products"
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Sales(models.Model):
    product = models.ForeignKey(Products, on_delete=None)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(default=0.00, max_digits=18, decimal_places=2)
    customer = models.ForeignKey(Auteur, on_delete=models.CASCADE, default='1')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title

    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        super(Sales, self).save(*args, **kwargs)

    class Meta:
        db_table = "tutorial_product_sales"
        verbose_name = "Sale"
        verbose_name_plural = "Sales"

        
