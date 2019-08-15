from django.db import models

VAT = (
    (0, "0"),
    (1, "0.05"),
    (2, "0.08"),
    (3, "0.23"),
)
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)

    def __str__(self):
        return " {} ".format(self.name)

class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    vat = models.IntegerField(choices=VAT)
    stock = models.IntegerField(default=0)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return "{} {}".format(self.name, self.price)
