from django import forms
from .models import Profile
from django.contrib.auth.models import User


class UserEditFroms(forms.ModelForm):
    
    class Meta:
        model =User
        fields = ['username','first_name','last_name','email']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'avatar')
