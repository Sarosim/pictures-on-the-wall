from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(), help_text='Minimum 8 characters long.')

    class Meta:
        model = User
        fields = ['email', 'username', 'password1']

    #Deleting the pw2 field from the form, according to the recent UX trends
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']
        #adding min length validator to password1 field
        password_field = self.fields['password1']
        password_field.validators.append(MinLengthValidator(limit_value=8))
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')

        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u"Oooops! Looks like You've already registered. Did You want to sign in? There's a sign in link just above this form.")
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if not password1:
            raise ValidationError("Please enter your password!")
        
        return password1