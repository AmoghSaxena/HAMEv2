# Import Porperties model from models.py
from .models import Properties

# Import forms from django
from django import forms

# Create a form for the Properties model
class PropertiesForm(forms.ModelForm):
    class Meta:
        model = Properties
        fields = ['title', 'address', 'postcode', 'description', 'specifications', 'price', 'photos', 'bedrooms', 'bathrooms', 'is_published', 'posted_by']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
            'specifications': forms.CheckboxSelectMultiple(),
            'posted_by': forms.HiddenInput()
        }

class PropertiesForm(forms.ModelForm):
    class Meta:
        model = Properties
        fields = ['title', 'address', 'postcode', 'description', 'specifications', 'price', 'bedrooms', 'bathrooms', 'is_published', 'posted_by']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
            'specifications': forms.CheckboxSelectMultiple(),
            'posted_by': forms.HiddenInput()
        }