from .models import Post, User
from .forms import LoginForm, RegisterForm, ProfileForm, LogoutForm, PostForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, is_authenticated
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
@is_authenticated
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

class ListView(viewsets.ViewSet):
    def list_posts(self, request):
        posts = Post.objects.all()
        return render(request, 'post_list.html', {'posts': posts})
    
class DetailView(viewsets.ViewSet):
    def post_detail(self, request, pk):
        post = Post.objects.get(pk=pk)
        return render(request, 'post_detail.html', {'post': post})

@login_required
class CreateView(viewsets.ViewSet):
    def create_post(self, request):
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'post_form.html', {'form': form})
    

@is_authenticated
@login_required
class UpdateView(viewsets.ViewSet):
    def update_post(self, request, pk):
        post = Post.objects.get(pk=pk)
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'post_form.html', {'form': form})

@login_required
@is_authenticated
class DeleteView(viewsets.ViewSet):
    def delete_post(self, request, pk):
        post = Post.objects.get(pk=pk)
        if request.method == 'POST':
            post.delete()
            return redirect('post_list')
        return render(request, 'post_confirm_delete.html', {'post': post})