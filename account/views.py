from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                form.save()
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
