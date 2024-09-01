from django.db import models

# Create your models here.
class Phone(models.Model): 
    model = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self): 
        return self.model
    