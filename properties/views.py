from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import Properties, Photos, Specifications, Likes, Views
from users.models import Profile

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listing(request):
    return render(request, 'index.html')

def property(request, id):
    context = {}
    if id == 200:
        profile = Profile.objects.get(user=request.user)
        context['profile_image'] = profile.image.url
        context['profile'] = profile
        return render(request, 'property_demo.html', context)
    try:
        prop = get_object_or_404(Properties, prop_id=id)
        context['property'] = prop
        context['list_date'] = str((prop.list_date).strftime("%dth %b %Y, %I:%M %p"))
        profile = Profile.objects.get(user=prop.posted_by.user)
        context['profile'] = profile
        # Get the photos for the property in a list
        list_of_photos = []
        try:
            context['photos'] = Photos.objects.filter(property_id=id).values()
            for photo in context['photos']:
                list_of_photos.append(photo['photo'])
            
            update_view = Views.objects.get(property=prop)
            update_view.views_count += 1
            update_view.save()
            context['property_views'] = update_view.views_count
        except:
            list_of_photos = ['/media/default.png']
        context['photos'] = list_of_photos
        print("##################")
        print(context)
        print(str((prop.list_date).strftime("%dth %b %Y, %I:%M %p")))
        print(context['photos'])
        print(list_of_photos)
        # print(context['property'].specifications.all())
        context['specs'] = []
        try:
            for spec in context['property'].specifications.all():
                context['specs'].append(spec.specifications)
        except:
            context['specs'] = ['No specifications']
        messages.success(request, f'{id}')
        return render(request, 'properties.html', context)
    except Exception as e:
        messages.error(request, f'error: {e}')
        print(e)
        return render(request, '404.html')

    

def propertyUpload(request):
    if request.method == 'POST':
        title = request.POST['title']
        address = request.POST['address']
        postcode = request.POST['postcode']
        description = request.POST['description']
        price = request.POST['price']
        bedrooms = 2
        bathrooms = 2.0
        photos = request.FILES.getlist('photos')
        mp_p = Profile.objects.get(user=request.user)
        user_logged_in = request.user
        # Create a new property
        new_property = Properties(title=title, address=address, postcode=postcode.upper(), description=description, price=price, bedrooms=bedrooms, bathrooms=bathrooms, posted_by=mp_p)
        new_property.save()
        
        # Add specifications to the property
        print("##################")
        print(request.POST.get('specification'))
        specifications = (request.POST.get('specification')).split(',')
        for spec in specifications:
            # check if the specification already exists
            if Specifications.objects.filter(specifications=spec.upper()).exists():
                new_spec = Specifications.objects.get(specifications=spec.upper())
            else:
                new_spec = Specifications(specifications=spec.upper())
                new_spec.save()

            new_property.specifications.add(new_spec)
        
        for photo in photos:
            # Create a new Photos instance
            new_photo = Photos(property=new_property, photo=photo)
            # Save the photo to the database
            new_photo.save()
            # Add the photo to the property's photos
            # new_property.photos.add(new_photo)
        new_property.save()
        
        #Add Views of the property
        new_view = Views(property=new_property)
        new_view.save()

        #Return Success message
        messages.success(request, 'Property added successfully')
        # Redirect to the property page with the new property id
        return redirect('property', new_property.prop_id)
        # return render(request, 'add_property.html')
    else:
        context = {}
        context['profile'] = Profile.objects.get(user=request.user)
        return render(request, 'add_property.html', context)
    
def editProperty(request, id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            # Check if the user is the owner of the property
            prop = get_object_or_404(Properties, prop_id=id)

            if request.user != prop.posted_by.user:
                messages.error(request, 'You are not authorized to edit this property')
                return redirect('home')
            
        prop = get_object_or_404(Properties, prop_id=id)
        prop.title = request.POST['title']
        prop.address = request.POST['address']
        prop.postcode = request.POST['postcode']
        prop.description = request.POST['description']
        prop.price = request.POST['price']
        prop.save()
        # Add specifications to the property
        print("##################")
        print(request.POST.get('specification'))
        specifications = (request.POST.get('specification')).split(',')
        # Clear the existing specifications
        prop.specifications.clear()
        for spec in specifications:
            # check if the specification already exists
            if Specifications.objects.filter(specifications=spec.upper()).exists():
                new_spec = Specifications.objects.get(specifications=spec.upper())
            else:
                new_spec = Specifications(specifications=spec.upper())
                new_spec.save()

            prop.specifications.add(new_spec)

        # Get the photos for the property in a list
        list_of_photos = []
        # Clear the existing photos
        Photos.objects.filter(property_id=id).delete()
        photos = request.FILES.getlist('photos')
        for photo in photos:
            # Create a new Photos instance
            new_photo = Photos(property=prop, photo=photo)
            # Save the photo to the database
            new_photo.save()
            # Add the photo to the property's photos
            # prop.photos.add(new_photo)
        prop.save()
    else:
        if request.user.is_authenticated:
            # Check if the user is the owner of the property
            prop = get_object_or_404(Properties, prop_id=id)

            if request.user != prop.posted_by.user:
                messages.error(request, 'You are not authorized to edit this property')
                return redirect('home')

        context = {}
        try:
            prop = get_object_or_404(Properties, prop_id=id)
            context['property'] = prop
            context['list_date'] = str((prop.list_date).strftime("%dth %b %Y, %I:%M %p"))
            profile = Profile.objects.get(user=prop.posted_by.user)
            context['profile'] = profile
            # Get the photos for the property in a list
            list_of_photos = []
            try:
                context['photos'] = Photos.objects.filter(property_id=id).values()
                for photo in context['photos']:
                    list_of_photos.append(photo['photo'])
            except:
                list_of_photos = ['/media/default.png']
            context['photos'] = list_of_photos
            print("##################")
            print(context)
            print(str((prop.list_date).strftime("%dth %b %Y, %I:%M %p")))
            print(context['photos'])
            print(list_of_photos)
            # print(context['property'].specifications.all())
            context['specs'] = []
            try:
                for spec in context['property'].specifications.all():
                    context['specs'].append(spec.specifications)
            except:
                context['specs'] = ['No specifications']
            messages.success(request, f'{id}')
            return render(request, 'edit_property.html', context)
        except:
            messages.error(request, 'Property not found')
            return render(request, '404.html')