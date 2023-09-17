from django.db import models

# Create your models here.
class products(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='/products',null = True,blank =True)
    def __str__(self):
        return self.title