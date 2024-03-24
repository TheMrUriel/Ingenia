from django.shortcuts import render
from ..models import *
from ..forms import CreateUserForm
from ..forms import LoginForm
from functools import wraps
from django.contrib.auth.models import auth
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, login, logout
from allauth.account.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect

def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:
        form = CreateUserForm()
    return render(request, 'Usuario/register.html', {'registerform': form})
    

def my_login(request):
    auth.logout(request)
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("/home/")
    context = {'loginform':form}
    return render(request, 'Usuario/login.html', context=context)

def user_logout(request):
    auth.logout(request)
    return redirect("/home/")

def user_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and Usuario.objects.filter(usuario=request.user).exists():
            return view_func(request, *args, **kwargs)
        else:
            return redirect("/login/")
    return _wrapped_view