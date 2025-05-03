from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Outfit(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('outfit-detail', kwargs={'outfit_id': self.id})

# Create your models here.
class Shoe(models.Model):
    brand = models.CharField(max_length=40)
    style = models.CharField(max_length=40)
    color = models.CharField(max_length=20)
    occasion = models.CharField(max_length=20)
    outfit = models.ManyToManyField(Outfit)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand} {self.style} ({self.color} {self.occasion})"
    
    def get_absolute_url(self):
        return reverse('shoe-detail', kwargs={'shoe_id': self.id})
    
