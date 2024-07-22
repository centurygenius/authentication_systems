from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        # Collect client details and process it

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        # Validate client password
        if password == confirm_password:

            # Check if email already exists
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('signup')
            
            # Check if username already exists
            elif User.objects.filter(username=username).exists():
                    messages.error(request, 'Username already exists')
                    return redirect('signup')
            
            # Create new user, save it and redirect to login page
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')           
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

def login(request):

    if request.method == 'POST':
        # Collect client details and process it
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        # Check if user exists
        if user is not None:
            auth.login(request, user)
            return redirect('success')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'login.html')

@login_required(login_url='login')
def success(request):
    return render(request, 'success.html')

def logoutUser(request):
    logout(request)
    return redirect('home')