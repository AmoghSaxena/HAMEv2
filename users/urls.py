from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .ClassBasedViews.UserManage import UserCreation, UserLogin

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', UserCreation.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/otp/', UserCreation.as_view(), name='otp'),

]