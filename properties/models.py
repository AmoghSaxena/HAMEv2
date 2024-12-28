from django.db import models
from users.models import Profile, User

# Create your models here.
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/photos/<posted_by>/<filename>
    return f'photos/{instance.property.posted_by.user.username}/{filename}'

class Photos(models.Model):
    photo_id = models.AutoField(primary_key=True)
    property = models.ForeignKey('Properties', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path)

    def __str__(self):
        return str(self.photo_id)

class Specifications(models.Model):
    spec_id = models.AutoField(primary_key=True)
    specifications = models.CharField(max_length=30)
    def __str__(self):
        return self.specifications

class Properties(models.Model):
    prop_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    postcode = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    specifications = models.ManyToManyField(Specifications, verbose_name="Specifications", blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
# class for likes for the properties
class Likes(models.Model):
    prop_id = models.ForeignKey(Properties, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    def __str__(self):
        return self.prop_id

# class for views for the properties
class Views(models.Model):
    property = models.ForeignKey(Properties, on_delete=models.CASCADE)
    views_count = models.IntegerField(default=0)
    def __str__(self):
        return self.property.title