from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            if user:
                messages.success(request,f'Accounts Created for {username}! You can now log in')
                login(request, user)
            return redirect('login')  

    else:
        form = UserRegisterForm()
    return render(request, 'register.html',{'form':form})

@login_required
def profile(request):
    return render(request, 'profile.html')


