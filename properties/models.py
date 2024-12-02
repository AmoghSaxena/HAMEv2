from django.db import models
from users.models import Profile

# Create your models here.

class Photos(models.Model):
    photo_id = models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    def __str__(self):
        return self.photo

class Specifications(models.Model):
    spec_id = models.AutoField(primary_key=True)
    specifications = models.CharField(max_length=30)
    def __str__(self):
        return self.specifications

class Properties(Photos):
    prop_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    postcode = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    specifications = models.ManyToManyField(Specifications, blank=True)
    price = models.IntegerField()
    photos = models.ManyToManyField(Photos, blank=True)
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
# class for likes for the properties
class Likes(models.Model):
    prop_id = models.ForeignKey(Properties, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.prop_id
    