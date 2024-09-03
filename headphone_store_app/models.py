from django.db import models

# Create your models here.
class Headphone(models.Model): 
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    stock = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    price = models.IntegerField()
    
    def __str__(self): 
        return self.brand + " " + self.model