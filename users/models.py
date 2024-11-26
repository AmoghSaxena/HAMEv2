from django.db import models
from newsletter.models import Subscribers
# Create your models here.

# Temoorary model for unverified users unless OTP testing is done
class TempUser(Subscribers):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return self.username