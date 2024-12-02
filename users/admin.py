from django.contrib import admin
from .models import TempUser, Profile


# Register your models here.

admin.site.register(TempUser)
admin.site.register(Profile)
