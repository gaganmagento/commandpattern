from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(f"User {user} saved and logged in")
            return redirect('home')  # Redirect to a home page or another page after registration
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def home(request):
    return render(request, 'home.html')