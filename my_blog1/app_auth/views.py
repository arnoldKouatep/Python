from traceback import print_tb
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import *

def login_blog(request):
   if request.method == "POST":
       form = LoginForm(request.POST)
       if form.is_valid():
           username = form.cleaned_data['username']
           pwd = form.cleaned_data['pwd']
           user = authenticate(username=username, password=pwd)
           if user is not None:
               login(request, user)
               return redirect('dashboard')
           else:
               messages.error(request, "Authentification echouee")
               return render(request, 'login.html', {'form':form})
        
       else:
           for field in form.errors:
               form[field].field.widget.attrs['class'] += '  is-valid'
           return render(request,"login.html", {'form':form})

   else:
       form = LoginForm()
       return render(request,"login.html", {'form':form})
    
    
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username =form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            user = User.objects.create_user(username=username, password =pwd)
            if user is not None:
                return redirect("login-blog")
            else:
                messages.error(request, 'creation de compte echouee')
                return render(request, 'register.html',{'form':form})
        else:
                            return render(request, 'register.html',{'form':form})
        return render(request, 'register.html', {})
    
    form = RegisterForm()
    return render(request, 'register.html', {'form':form})


def logout_blog(request):
    logout(request)
    return redirect('login-blog')
    