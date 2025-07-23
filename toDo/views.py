from django.shortcuts import render, redirect
from django.views import View 
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
import json
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
from .models import Task

# Create your views here.
class homeView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    def get(self,request):
        todo = request.user.tasks.all()
        return render(request,'home.html', {'todo': todo})


class addTask(LoginRequiredMixin,View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def post(self, request):
        task = request.POST.get('newTask')

        if not task:
            return redirect('home')
        
        if task:
            request.user.tasks.create(task=task)
        return redirect('home')


class delete_task(LoginRequiredMixin,View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def post(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id, user=request.user)
            task.delete()
        except Task.DoesNotExist:
            pass
        return redirect('home')


class update_task(LoginRequiredMixin,View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def post(self, request, task_id):
        try:
            task = Task.objects.get(id=task_id, user=request.user)
            task.completed = not task.completed
            task.save()
        except Task.DoesNotExist:
            pass
        return redirect('home')




class registerView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'register.html', {'form': form})



class loginView(View):
    def get(self, request): 
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return render(request, 'login.html', {'error': 'Please enter both username and password'})

        user = authenticate(request, username=username, password=password)  
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})



class logoutView(View):
    def post(self, request):
        logout(request)
        return redirect('login')