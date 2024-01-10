from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # throw message when any fields are wrong while registering
            user = form.cleaned_data.get('username')
            messages.success(request,"Account created for "+ user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'loginApp/register.html', context)

def userlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('feed')
        else:
            messages.info(request, "username or password is incorrect")

    return render(request, 'loginApp/login.html')

def userlogout(request):
    logout(request)
    return redirect('login')
