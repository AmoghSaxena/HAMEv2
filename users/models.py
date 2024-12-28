from django.db import models
from newsletter.models import Subscribers
from django.contrib.auth.models import User
# Create your models here.

# Temoorary model for unverified users unless OTP testing is done
class TempUser(Subscribers):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    is_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.username
    
# Profile model for storing user details
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    image = models.ImageField(upload_to='profile_pics', default='default.png')
    
    def __str__(self):
        return self.user.username
    
# class for ratings for the users
class Ratings(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    
    def __str__(self):
        return self.user_id