from django import forms
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm

from .models import Profile , User


class RegisterForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=100 , 
                                 required=True,
                                 widget= forms.TextInput(attrs= {'placeholder':'First Name' , 
                                                                 'class':'form-control' ,}))
    
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget= forms.TextInput( attrs= {'placeholder':'Last Name',
                                                                 'class':'form-control'}))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget= forms.TextInput(attrs={'placeholder':'Username',
                                                              'class':'form-control'}))
    email = forms.EmailField(required=True,
                             widget= forms.TextInput(attrs={'placeholder':'Email',
                                                            'class':'form-control'}))
    password1 = forms.CharField(max_length=50 , 
                                required=True,
                                widget= forms.PasswordInput(attrs={'placeholder':'Password',
                                                                   'class':'form-control',
                                                                   'data-toggle':'password',
                                                                   'id':'password'}))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget= forms.PasswordInput(attrs={'placeholder':'Confirm Password',
                                                                   'class':'form-control',
                                                                   'data-toggle':'password',
                                                                   'id':'password'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']