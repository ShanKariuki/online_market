from django.shortcuts import render,redirect
from store.models import *
from .forms import *
from django.contrib.auth import logout

def signup(request):
    if request.method == 'POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
     form=SignupForm()
    return render(request,'accounts/signup.html',{'form':form})


def sign_out(request):
    logout(request)
    return redirect('store:index')