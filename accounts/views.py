from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth import login , logout , authenticate
from .forms import RegisterForm , UpdateUserForm
from .models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def registerPage(request):
    form = RegisterForm()
    
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            login(request , user)
            return redirect('home')
        else:
            messages.error(request , 'Something occurred during registration')
            
    context = {'form':form}
    return render(request , 'accounts/register.html', context)
            
def loginPage(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    
    
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
            
        except :
            user = User.objects.get(username=email)
            if user is None:
                messages.error(request , 'User does not exist')

        try:
            user_x = User.objects.get(username=email)
            user = authenticate(request , email=user_x.email , password=password)
        except:
            user = authenticate(request , email=email , password=password)
            
        #user = authenticate(request , email=email , password=password)
        
        if user is not None:
            login(request , user)
            return redirect('home')
        else:
            messages.error(request , 'email or password is wrong')
        
    context = {}
    return render(request , 'accounts/login.html' , context)


def logoutPage(request):
    
    logout(request)
    return redirect('home')
    
                

def home(request):
    
    return render(request , 'accounts/home.html')


@login_required(login_url='login')
def profile(request , pk):
    user = User.objects.get(id=pk)
    
    context = {'user':user}
    return render(request , 'accounts/profile.html' , context)


@login_required(login_url='login')
def updateProfile(request):
    user = request.user 
    form = UpdateUserForm(instance=user)
    
    if request.method == 'POST':
        form = UpdateUserForm(request.POST , request.FILES , instance=user)
        
        if form.is_valid():
            form.save()
            return redirect('profile' , pk=user.id)
    
    context = {'form':form}
    return render(request , 'accounts/update_user.html' , context)