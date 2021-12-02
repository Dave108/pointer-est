from django.contrib import admin
from .models import Folder, ImagesPin, UserImage, Tag, ImageTest, FavImage, Comment, PinUser
from django import forms

# admin headings customizations
admin.site.site_header = "LOGIN TO POINTER-EST"
admin.site.site_title = "WELCOME TO ADMIN"
admin.site.index_title = "SCI-FI PORTAL"


# Register your models here.
@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'slug', 'folder_image']  # for showing desired fields in the page
    list_display_links = ['id']  # making a filed clickable to open the desired row
    list_editable = ['name']  # making a field editable from the outside
    search_fields = ['user', 'name']  # search using the fields
    ordering = ['name']  # ordering by field
    list_filter = ['name', 'user']  # filtering by the list

    # fields = ['user', 'name']
    # exclude = ['name']
    fieldsets = [
        ('USER ASSOCIATED', {'fields': ['user']}),
        ('FOLDER NAME', {'fields': ['name', 'slug', 'folder_image']}),
    ]  # for adding headings to the desired fields

    radio_fields = {'user': admin.HORIZONTAL}  # for adding radio filed to the filed which has more than one choice


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'word', 'count', 'created_at']


@admin.register(FavImage)
class FavImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'imagesPin', 'user']


@admin.register(ImagesPin)
class ImagesPinAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'image_name', 'slug', 'description', 'created_by']

    list_display_links = ['id']
    list_editable = ['image_name']
    search_fields = ['image_name', 'id']
    ordering = ['image_name']
    list_filter = ['image_name', 'id']

    fields = ['image', 'image_name', 'slug', 'tags', 'description', 'created_by']
    # exclude = ['name']
    # raw_id_fields = ['tags']
    prepopulated_fields = {'slug': ['image_name']}


@admin.register(UserImage)
class UserImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'imagesPin', 'folder', 'user']

# @admin.register(ImageTest)
# class UserImageAdmin(admin.ModelAdmin):
#     list_display = ['id', 'image']
#
#     readonly_fields = ('thumbnail_preview',)
#
#     def thumbnail_preview(self, obj):
#         return obj.thumbnail_preview
#
#     thumbnail_preview.short_description = 'Thumbnail Preview'
#     thumbnail_preview.allow_tags = True


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'pin', 'user', 'body', 'creation_date', 'edited', 'parent']


@admin.register(PinUser)
class PinUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'gender', 'age']
