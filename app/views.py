from django.shortcuts import render
from .models import Folder, ImagesPin, UserImage


# Create your views here.

def home_view(request):
    images = ImagesPin.objects.all()
    print(images)
    context = {
        "images": images
    }
    return render(request, 'home.html', context)


def create_folder(request):
    name = "name_test"
    Folder.objects.create(
        user=request.user,
        name=name,
    )

