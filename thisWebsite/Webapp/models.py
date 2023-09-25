from django.db import models
class Person(models.Model):  # Updated class name to follow naming conventions
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    def __str__(self):
        return self.first_name + self.last_name

class Product(models.Model):  # Updated class name to follow naming conventions
    product_title = models.CharField(max_length=225)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_brand = models.CharField(max_length=225)
    product_images = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.product_title
