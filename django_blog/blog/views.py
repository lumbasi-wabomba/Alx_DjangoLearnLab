from .models import Post, User
from .forms import LoginForm, RegisterForm, ProfileForm, LogoutForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required   
from rest_framework import viewsets


class LoginView(viewsets.ViewSet):
    def login(self, request):
        if request.method == 'POST':
            form = LoginForm(request, data=request.POST)
            if form.is_valid():
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    return redirect('profile')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})
    
class LogoutView(viewsets.ViewSet):
    def logout(self, request):
        if request.method == 'POST':
            logout(request)
            return redirect('login')
        form = LogoutForm()
        return render(request, 'logout.html', {'form': form})
    

class RegisterView(viewsets.ViewSet):
    def register(self, request):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('profile')
        else:
            form = RegisterForm()
        return render(request, 'register.html', {'form': form})
    
@login_required
class ProfileManagementView(viewsets.ViewSet):
    def update_profile(self, request):
        user = request.user
        if request.method == 'POST':
            form = ProfileForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect('profile')
        else:
            form = ProfileForm(instance=user)
        return render(request, 'profile.html', {'form': form})
    
    def view_profile(self, request):
        user = request.user
        return render(request, 'profile.html', {'user': user})
    
    def delete_profile(self, request):
        if request.method == 'POST':
            user = request.user
            user.delete()
            logout(request)
            return redirect('login')
        return render(request, 'delete_profile.html', {'user': request.user})

