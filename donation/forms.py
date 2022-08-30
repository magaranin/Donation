from dataclasses import fields
from django import forms
from .models import ListingOffer, Category
from django.forms import Textarea, ModelForm

class NewListingForm(forms.ModelForm):
    class Meta:
        model = ListingOffer
        fields = ['title', 'description', 'gender', 'categories', 'images', 'who_pays', 'shipping_cost']
        label = {
            'shipping_cost': ''
        }
        widgets = {
            'title':Textarea(attrs={'class': 'form-control', 'rows' : 1}),
            'description': Textarea(attrs={'class': 'form-control', 'rows' : 2}),
            'images': forms.FileInput(attrs={'id':'myfile','class':'form-control-file','multiple':True}),
        }

