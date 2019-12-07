from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from authentication.forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required

def index(request):
    """Return teh index.html page"""
    return render(request, 'index.html')

def logout(request):
    """Log the user out..."""  
    auth.logout(request)
    messages.success(request, "You have successfully been logged out.")
    return redirect(reverse('index'))
    
def login(request):
    """Return the LOGIN page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(
                username=request.POST['username'],
                password=request.POST['password']
            )
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully been logged in.")
            else:
                login_form.add_error(None, "Username or Password is incorrect!")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form":login_form})
