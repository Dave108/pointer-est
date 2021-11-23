from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import Folder, ImagesPin, UserImage
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model


# Create your views here.

def home_view(request):
    if request.method == "POST":
        print(request.POST)
        # if "sign-in" in request.POST:
        #     print(request.POST)
    images = ImagesPin.objects.all()
    # print(images[0:12])
    context = {
        "images": images[0:18]
    }
    return render(request, 'home.html', context)


def create_folder(request):
    name = "name_test"
    Folder.objects.create(
        user=request.user,
        name=name,
    )


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        print("inside login view")
    return HttpResponseRedirect('/user-panel/')


def registration(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(username, email, password)
        print("inside registration view")
    return HttpResponseRedirect(reverse('homepage'))


def user_panel_view(request):
    return render(request, 'user_panel.html')
