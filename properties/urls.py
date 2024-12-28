from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('property/<int:id>', views.property, name='property'),
    path('add_property/', login_required(views.propertyUpload), name='add_property'),
    path('edit_property/<int:id>', login_required(views.editProperty), name='edit_property'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)