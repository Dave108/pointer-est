from django.contrib import admin
from .models import Folder, ImagesPin, UserImage


# Register your models here.
@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name']


@admin.register(ImagesPin)
class ImagesPinAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'tags']


@admin.register(UserImage)
class UserImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'imagesPin', 'folder']
