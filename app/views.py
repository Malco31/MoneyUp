

from app.forms import *
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from app.forms import *
from .decorators import admin_only
from .models import Wages


# Import Models



#
# Create your views here.

def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            group = Group.objects.get(name='not_admin')
            user.groups.add(group)
            return redirect('login')
    return render(request, 'signup.html', {'form':form})

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('frontpage')
        else:
            messages.info(request, "Username or password is incorrect!")
    return render(request, 'login.html')
    

def signout(request):
    logout(request)
    return redirect('login')

def clockout(request):
    form = ClockoutForm()
    if request.method == 'POST':
        form = ClockoutForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Successfully clocked out!')
    return render(request, 'clockout.html', {'form':form})

@login_required(login_url='login')
def frontpage(request):
    if request.method == "POST":
        print(request.user)
        return render(request, 'frontpage.html')
    else:
        print("fail")
        return render(request, 'frontpage.html')

@login_required
def myaccount(request):
    my_entries = Entry.objects.filter(user= request.user)
    initial_hours = 0
    mins_to_hours = 0
    for entry in my_entries:
        initial_hours += entry.hours
        mins_to_hours += entry.minutes / 60
    total_hours = mins_to_hours + initial_hours
    wage = Wages.objects.get(user=request.user)
    total_earned = wage.payrate * total_hours
    return render(request, 'myaccount.html', {'entries':my_entries, 'total_hours':total_hours, 'total_earned':total_earned})

@login_required
@admin_only
def admin_account(request):
    all_entries = Entry.objects.all()
    return render(request, 'admin_account.html', {'entries':all_entries})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        request.user.first_name = request.POST.get('first_name', '')
        request.user.last_name = request.POST.get('last_name', '')
        request.user.email_name = request.POST.get('email_name', '')
        request.user.save()

        messages.info(request, 'The changes were saved')

        return redirect('myaccount')

    return render(request, 'edit_profile.html')

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)

#         if form.is_valid():
#             user = form.save()
#             user.email= user.username
#             user.save()

#             userprofile = Userprofile.objects.create(user=user)

#             login(request, user)
#             logout(request, user)

#             return redirect('frontpage', user)
        
#     else:
#         form = UserCreationForm()

#     return render(request, 'signup.html', {'form':form})


    # mins_to_hours = minutes / 60
    # total_hours = mins_to_hours + hours
    # total_earned = payrate * total_hours
   