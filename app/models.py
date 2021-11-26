from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html
from django.utils.html import mark_safe


# Create your models here.
class Folder(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    folder_image = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    word = models.CharField(max_length=35)
    count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word


class ImagesPin(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=200)
    slug = models.CharField(max_length=250)
    tags = models.ManyToManyField(Tag, related_name='photos')
    description = models.TextField(null=True)

    def __str__(self):
        return self.image_name

    @property
    def thumbnail_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.image.url))
        return ""
    # @property
    # def thumbnail_preview(self):
    #     if self.image:
    #         _thumbnail = get_thumbnail(self.image,
    #                                    '300x300',
    #                                    upscale=False,
    #                                    crop=False,
    #                                    quality=100)
    #         return format_html(
    #             '<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
    #     return ""


class UserImage(models.Model):
    imagesPin = models.ForeignKey(ImagesPin, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.folder.name


class ImageTest(models.Model):
    image = models.ImageField('image')

    @property
    def thumbnail_preview(self):
        if self.image:
            _thumbnail = get_thumbnail(self.image,
                                       '300x300',
                                       upscale=False,
                                       crop=False,
                                       quality=100)
            return format_html(
                '<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""
