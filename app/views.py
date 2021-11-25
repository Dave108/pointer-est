from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from .models import Folder, ImagesPin, UserImage, Tag
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm


# Create your views here.

def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/user-panel/')
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
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/user-panel/')
    return HttpResponseRedirect('/user-panel/')


def registration(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        all_users = User.objects.all()
        for user in all_users:
            # print(user.username)
            # print(user.email)
            if user.username == username:
                print("Username exists already!")
                return HttpResponseRedirect(reverse('homepage'))
            if user.email == email:
                print("Email exists already!")
                return HttpResponseRedirect(reverse('homepage'))

        if not password == password2:
            print("passwords are not equal")
            return HttpResponseRedirect(reverse('homepage'))
        if len(password) <= 8:
            print("password should be more that 8 letters")
            return HttpResponseRedirect(reverse('homepage'))
        print(username, email, password, password2)
        print("inside registration view")
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            if user:
                print(user)
                print("User created successfully!!!")
        except:
            print("User name is already available!!!")

    return HttpResponseRedirect(reverse('homepage'))


@login_required(login_url="homepage")
def user_panel_view(request):
    print("---- Inside user panel")
    images = ImagesPin.objects.all()
    context = {
        "images": images
    }
    return render(request, 'user_panel.html', context)


def select_folder(request):
    all_folders = Folder.objects.filter(user=request.user)
    context = {
        "folders": all_folders,
    }
    return render(request, 'select_folder.html', context)


def save_image(request):
    return HttpResponse("<h1>save image</h1>")
