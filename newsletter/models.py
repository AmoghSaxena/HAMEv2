from django.db import models

# Create your models here.

class Subscribers(models.Model):
    email = models.EmailField(max_length=50)
    
    def __str__(self):
        return self.email
    