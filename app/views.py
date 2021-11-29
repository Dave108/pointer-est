from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from .models import Folder, ImagesPin, UserImage, Tag, FavImage
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
import re
import cloudinary


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
    images = None
    # user_img = [u_img.imagesPin.id for u_img in UserImage.objects.exclude(user=request.user)]
    user_img = [u_img.imagesPin.id for u_img in UserImage.objects.filter(user=request.user)]
    print(user_img)
    if user_img:
        # images = user_img.pinimages_set.exclude(user=request.user)

        # images = ImagesPin.objects.filter(id__in=user_img)
        images = ImagesPin.objects.exclude(id__in=user_img)
        print(images)
    else:
        images = ImagesPin.objects.all()
    context = {
        "images": images
    }
    return render(request, 'user_panel.html', context)


@login_required(login_url="homepage")
def select_folder(request):
    all_folders = Folder.objects.filter(user=request.user)
    context = {
        "folders": all_folders,
    }
    return render(request, 'select_folder.html', context)


def save_image(request):
    return HttpResponse("<h1>save image</h1>")


def slug_the_name(pinname):
    name = pinname.replace(' ', '-').lower()
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    regex_list = ["[", "@", "_", "!", "#", "$", "%", "^", "&", "*", "(", ")", "<", ">", "?", "/", "\\", "|", "}", "{",
                  "~", ":", "]"]
    print(len(regex_list))
    for reg in regex_list:
        if reg in name:
            name = name.replace(reg, '')
    # Pass the string in search
    # method of regex object.
    if regex.search(name) is None:
        print("String is accepted")
        return name
    else:
        print("String is not accepted.")
    return name


def create_tags(tag):
    tag_list = []
    tag_list = tag.split(',')
    send_tags = []
    for tg in tag_list:
        tg = slug_the_name(tg)
        try:
            tag2 = Tag.objects.get(word=tg)
        except:
            tag2 = Tag.objects.create(
                word=tg,
                count=1,
            )
        send_tags.append(tag2)
    return send_tags


def create_folder_slug(name):
    print(name, "---inside create folder slug")
    name = slug_the_name(name)
    print(name, "---After slugifying the name")
    exist_slug = Folder.objects.filter(slug=name).exists()

    if exist_slug:

        name = name + "uni"
        print(name)
        return name
    else:
        print(name)
        return name


@login_required(login_url="homepage")
def my_pins(request):
    folders = Folder.objects.filter(user=request.user)
    tags = Tag.objects.all()

    context = {
        "folders": folders,
        "tags": tags,
    }
    return render(request, 'my_pins.html', context)


def add_unorganised_folder(user_for_folder, url):
    folder = Folder.objects.filter(user=user_for_folder, name="Unorganised pins").first()
    if folder:
        return folder
    else:
        folder = Folder.objects.create(
            user=user_for_folder,
            name="Unorganised pins",
            slug="unorganised-pins",
            folder_image=url,
        )
        return folder


@login_required(login_url="homepage")
def create_pin(request):
    # for saving pins --------------------
    if request.method == "POST":
        new_folder = ''
        # print(request.POST)
        pinname = request.POST.get('pin-name')
        desc = request.POST.get('description')
        image = request.FILES.get('image')

        # slugifying the image name by calling a funtion made for it
        slugged_name = slug_the_name(pinname)
        # print(slugged_name)
        pinned_image = ImagesPin.objects.create(
            image=image,
            image_name=pinname,
            description=desc,
        )
        if ImagesPin.objects.filter(slug=slugged_name).exists():
            pinned_image.slug = slugged_name + str(pinned_image.id)
            pinned_image.save()
        else:
            pinned_image.slug = slugged_name
            pinned_image.save()

        if request.POST.get('board') == "---- Select A Board ----":
            board = request.POST.get('new-board')
            # print(board, '---board here')
            if board:
                # print("if ran")
                try:
                    new_folder = Folder.objects.get(user=request.user, name=board)
                    print("try ran")
                except:
                    print("except ran")
                    folder_slug = create_folder_slug(board)

                    new_folder = Folder.objects.create(
                        user=request.user,
                        name=board,
                        folder_image=pinned_image.image.url,
                    )
                    if "uni" in folder_slug:
                        print("not unique")
                        new_folder.slug = folder_slug + str(new_folder.id)
                        new_folder.save()
                    else:
                        new_folder.slug = folder_slug
                        new_folder.save()

        else:
            board = request.POST.get('board')
            print(board, 'lower board')
            if board:
                new_folder = Folder.objects.get(id=board)
                print(new_folder)
        print(new_folder, 'new-----folder')
        if request.POST.get('tag') == "---- Select A Tag ----":
            print("equal tag")
            tag = request.POST.get('new-tag')
            print(tag, "upper tag here----")
            if tag:
                tag = create_tags(tag)
            print(tag, '--------------')
        else:
            print("not equal tag")
            tag = request.POST.get('tag')
            print(tag, 'tag----------------------------------')
            if tag:
                tag = Tag.objects.get(id=tag)
        print(tag, "final value --------")
        try:
            pinned_image.tags.set(tag)
        except:
            pinned_image.tags.add(tag)
        pinned_image.save()
        print(new_folder, '-----------end ', tag)

        if new_folder:
            print(new_folder)
            UserImage.objects.create(
                imagesPin=pinned_image,
                folder=new_folder,
                user=request.user,
            )
        else:
            user_for_folder = request.user
            url = pinned_image.image.url
            unorganised_folder = add_unorganised_folder(user_for_folder, url)
            UserImage.objects.create(
                imagesPin=pinned_image,
                folder=unorganised_folder,
                user=request.user,
            )
    return HttpResponseRedirect('/my-pins/')


@login_required(login_url="homepage")
def open_folder(request, slug):
    folder = Folder.objects.get(slug=slug)
    folder_images = UserImage.objects.filter(folder=folder)
    context = {
        "images": folder_images,
        "board_name": folder.name,
    }
    return render(request, 'my_folder.html', context)


@login_required(login_url="homepage")
def fav_pin(request, pk):
    print(pk)
    image = ImagesPin.objects.get(id=pk)
    try:
        print("try")
        img = FavImage.objects.get(imagesPin=image, user=request.user)
        if img:
            img.delete()
        else:
            FavImage.objects.create(imagesPin=image, user=request.user)
    except:
        print("exception")
        FavImage.objects.create(imagesPin=image, user=request.user)
    return HttpResponseRedirect('/user-panel/')


@login_required(login_url="homepage")
def my_fav_pins(request):
    if request.method == "GET":
        id = request.GET.get('action')
        print(id)
        try:
            fav_img = FavImage.objects.get(id=id)
            fav_img.delete()
        except:
            pass
    images = FavImage.objects.filter(user=request.user)
    context = {
        "images": images
    }
    return render(request, 'fav_pins.html', context)
