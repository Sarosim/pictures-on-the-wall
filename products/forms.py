from django import forms
from .models import Product, Artist, Hashtag, Size, Badge

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image',]
    
    # your_file = forms.ImageField(label='Select your file')

class EditProductFormOne(forms.ModelForm):
    """ Part 1 of the form for editing or uploading a new artwork
    This is the first column for the title, description and image """
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'image',
            'category',
            'room',
            'available_technologies',
            'base_repro_fee',
            'artist',
        ]
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control myform-title'
                    # where form-control is Bootstrap while myform-title is 
                    # my own class to be used in my stylesheet for formating
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control myform-description'
                }
            ),
            'artist': forms.HiddenInput(
                attrs={
                    'class': 'not-needed',
                    # 'value': ''
                }
            ),
        }


class EditProductFormThree(forms.ModelForm):
    """ Part 3 of the form for editing or uploading a new artwork
    This is the last column for the hashtags """
    class Meta:
        model = Hashtag
        fields = ['hashtag']


class ArtistProfileForm(forms.ModelForm):
    """ A form for creating or editing Artist profile information"""
    class Meta:
        model = Artist
        fields = [
            'first_name',
            'last_name',
            'artist_name',
            # 'avatar', -- potential feature, currently out of scope
            'badge',
            'address',
            'wants_marketing',
            'wants_newsletter',
            'assigned_user',
        ]
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'required': True,
                    'class': 'form-control artist-form-first_name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control artist-form-last_name'
                }
            ),
            'artist_name': forms.TextInput(
                attrs={
                    'required': True,
                    'class': 'form-control artist-form-artist_name'
                }
            ),
            'badge': forms.Select(
                attrs={
                    'class': 'form-control artist-form-badge'
                }
            ),
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control artist-form-address'
                }
            ),
            'wants_marketing': forms.CheckboxInput(
                attrs={
                    'title': 'Would You like to receive marketing communication?',
                    'class': 'form-control artist-form-marketing'
                }
            ),
            'wants_newsletter': forms.CheckboxInput(
                attrs={
                    'title': 'Would You like to receive our infrequent newsletters?',
                    'class': 'form-control artist-form-newsletter'
                }
            ),
            'assigned_user': forms.HiddenInput(
                attrs={
                    'class': 'form-control artist-form-hidden'
                }
            ),
        }
        labels = {
            'artist_name': 'Display Name',
            'wants_newsletter': 'Request newsletter',
            'wants_marketing': 'Request marketing communication',
        }
