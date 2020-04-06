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
        fields = ['title', 'description', 'image','category', 'room', 'available_technologies', 'base_repro_fee', 'artist']
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
