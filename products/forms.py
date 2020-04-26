from django import forms
from .models import Product, Artist, Hashtag, Size, Badge, Rating

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
            'room': forms.SelectMultiple(
                attrs={
                    'title': 'You can select multiple choices by holding the Ctrl/Command button down',
                    'class': 'room-dropdown',
                }
            ),
            'available_technologies': forms.SelectMultiple(
                attrs={
                    'title': 'You can select multiple choices by holding the Ctrl/Command button down\n Select as many as you can',
                    'class': 'technologies-dropdown',
                }
            ),
        }


class EditProductFormThree(forms.ModelForm):
    """ Part 3 of the form for editing or uploading a new artwork
    This is the last column for the hashtags """
    class Meta:
        model = Hashtag
        fields = ['hashtag']


class SizeForm(forms.ModelForm):
    """ create the size variants programmatically with a util function"""
    class Meta:
        model = Size
        fields = [
            'format_name',
            'size_name',
            'longer_side',
            'shorter_side',
            ]

class RatingForm(forms.ModelForm):
    """ The form for adding a rating to the database """
    
    rating = forms.ChoiceField(
                label='Your rating',
                choices = [(i, i) for i in range(1, 6)],
                required=True)

    class Meta:
        model = Rating
        fields = [
            'product',
            'rating',
        ]

        widgets = {
            'product': forms.HiddenInput(
                # attrs={
                #     'class': 'not-needed',
                #     # 'value': ''
                # }
            ),
        }

class SortForm(forms.Form):
    """Form to select the sort field """

    SORT_CHOICES = [
        'category', 
        'num_of_orders', 
        'num_of_views', 
        'date_uploaded'
    ]

    sort_field = forms.ChoiceField(label='Sort by', choices=SORT_CHOICES, required=False)