from django.db import models

class Person(models.Model):  # Updated class name to follow naming conventions
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    def __str__(self):
        return self.first_name +" "+ self.last_name

class Product(models.Model):  # Updated class name to follow naming conventions
    title = models.CharField(max_length=225)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Corrected upload_to path

    def __str__(self):
        return self.title
