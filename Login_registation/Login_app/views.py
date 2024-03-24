from django.shortcuts import render
from Login_app.forms import UserForm, UserInfoForm
from django.contrib.auth.models import User
from .models import UserInfo
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    context = {}
    if request.user.is_authenticated:
        current_user = request.user
        user_id = current_user.id
        user_basic_info = User.objects.get(pk=user_id)
        user_more_info = UserInfo.objects.get(user__pk=user_id)
        context = {'user_basic_info': user_basic_info, 'user_more_info': user_more_info}
    return render(request, 'Login_app/index.html', context=context)


def login_page(request):
    return render(request,'Login_app/login.html')
 
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        User = authenticate(username = username, password = password)
        
        if User:
            if User.is_active:
                login(request, User)
                return HttpResponseRedirect(reverse('Login_app:index'))
            else:
                return HttpResponse("Account is not active!!")
        else:
            return HttpResponse("Invalid login details provided")
    return render(request, 'Login_app/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login_app:index'))

def register(request):
    register = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        user_info_form = UserInfoForm(request.POST, request.FILES)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.user = user
            if 'profile_pic' in request.FILES:
                user_info.profile_pic = request.FILES['profile_pic']
                user_info.save()
                register = True
    else:
        user_form = UserForm()
        user_info_form = UserInfoForm()
    
    context = {'user_form':user_form, 'user_info_form':user_info_form, 'register':register}
    return render(request, 'Login_app/register.html', context=context)
