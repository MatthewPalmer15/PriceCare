from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from Users.forms import CreateUser

def view_user(request):
    return render(request, "users/view.html", {})

def register_user(request):
    if request.user.is_authenticated:
        redirect("/")
    if request.method == "POST":
        form = CreateUser(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            for error in form.errors:
                messages.error(request, form.errors[error][0], extra_tags='danger')
            return render(request, "users/register.html", {'form': form})
        return redirect("/")
    else:
        form = CreateUser()
        return render(request, "users/register.html", {'form': form})

def login_user(request):
    if request.user.is_authenticated:
        redirect("/")
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"You are now logged in as {request.user.username}", extra_tags='success')        
            return redirect("/")
        else:
            messages.error(request, "Invalid Username or Password. Please Try Again", extra_tags='danger')
            return render(request, 'users/login.html', {"error_message":"Account has not been found. Please Try again"})
    else:
        return render(request, 'users/login.html', {})

def logout_user(request):
    logout(request=request)
    request.session.clear()
    messages.success(request, "You have been logged out", extra_tags='success')
    return redirect("/")
