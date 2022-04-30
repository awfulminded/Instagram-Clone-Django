from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


def signin_view(request):
    if request.user.is_authenticated:
        return redirect('home_url')
    return render(request, 'auth/signin.html')

def home_view(request):
    if request.user.is_authenticated:
        return render(request, 'home/home.html')
    return redirect('signin_url')

def signup_view(request):
    if is_auth(request) != True:
        return render(request, 'auth/signup.html')
    return redirect('home_url')

def signin_user(request):
    if request.method == 'POST':
        if is_auth(request) != True:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(username=username, password=password, email=email)
            if user is not None:
                login(request, user)
            else:
                return JsonResponse({'status': 'incorrect data'})
            return JsonResponse({'status': 'success'})

def signup_user(request):
    if request.method == 'POST':
        if is_auth(request) != True:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            if validate_data(username, email, password) == True:
                try:
                    user = User.objects.create_user(username, email, password)
                    user.save()
                    new_profile = Profile.objects.create(username=username, owner = user)
                    new_profile.save()
                    login(request, user)
                except:
                    return JsonResponse({'status': 'something went wrong'})
            else:
                return JsonResponse({'status': 'data stupid'})
            return JsonResponse({'status': 'success'})


def update_pic(request):
    if request.method == 'POST':
        if is_auth(request):
            avatar = request.FILES.get('avatar')
            print('ava')
            print(avatar)
            profile = Profile.objects.get(username = request.user.username)
            profile.avatar = avatar
            profile.save()
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'not auth'})
    return JsonResponse({'status': 'not 500'})



def profile_page(request, user_page):
    if is_auth(request):
        try:
            avatar = ('media/' + str((Profile.objects.get(username=user_page)).avatar))
            username = (Profile.objects.get(username=user_page)).username
            return render(request, 'profile/profile.html', context={'username': user_page, 'avatar': avatar})
        except:
            return render(request, '404/404.html', context={'current_user': user_page})
    return redirect('signin_url')


def is_auth(request):
    if request.user.is_authenticated:
        return True
    return False

def validate_data(username, email, password):
    if ' ' not in username and ' ' not in password and ' ' not in email:
        if '@' in email and '.' in email:
            if username == username.lower():
                return True
    print('false')
    return False
