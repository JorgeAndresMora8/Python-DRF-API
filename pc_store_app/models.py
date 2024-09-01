from django.db import models

# Create your models here.
class Computer(models.Model): 
    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    def __str__(self): 
        return self.model + " " + self.brand
    