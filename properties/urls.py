from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='home'),
    path('property/<int:id>', views.property, name='property'),
    path('add_property/', login_required(views.testUpload), name='add_property'),
]