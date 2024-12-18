from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import Properties, Photos, Specifications

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listing(request):
    return render(request, 'index.html')

def property(request, id):
    messages.success(request, f'{id}')
    return render(request, 'properties.html')

def testUpload(request):
    if request.method == 'POST':
        title = request.POST['title']
        address = request.POST['address']
        postcode = request.POST['postcode']
        description = request.POST['description']
        price = request.POST['price']
        bedrooms = 2
        bathrooms = 2.0
        specifications = ['spec1', 'spec2']
        photos = request.FILES.getlist('photos')
        
        # Create a new property
        new_property = Properties(title=title, address=address, postcode=postcode, description=description, price=price, bedrooms=bedrooms, bathrooms=bathrooms)
        new_property.save()
        
        # Add specifications to the property
        for spec in specifications:
            new_spec = Specifications(specifications=spec)
            new_spec.save()
            new_property.specifications.add(new_spec)
        
        for photo in photos:
            # Create a new Photos instance
            new_photo = Photos(photo=photo)
            # Save the photo to the database
            new_photo.save()
            # Add the photo to the property's photos
            new_property.photos.add(new_photo)

        return render(request, 'add_property.html')
    else:
        specs = Specifications.objects.all()
        return render(request, 'add_property.html', {'specs': specs})