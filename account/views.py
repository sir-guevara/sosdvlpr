from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from .forms import UserEditFroms, ProfileEditForm


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                new_user = form.save()
                profile = Profile.objects.create(user=new_user)
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('index')
                else:
                    return redirect('login')
    
    else:
        logout(request)
        form = UserCreationForm
    context = {'form':form}
    return render(request,'registration/register.html',context)





