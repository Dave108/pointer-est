from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html
from django.utils.html import mark_safe
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Folder(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=250)
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
    created_by = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

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
    imagesPin = models.ForeignKey(ImagesPin, on_delete=models.CASCADE, related_name="pinimages")
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)


class FavImage(models.Model):
    imagesPin = models.ForeignKey(ImagesPin, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)


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


class Comment(models.Model):
    pin = models.ForeignKey(ImagesPin, on_delete=models.CASCADE, related_name="pins")
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    body = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name="+")
    likes = models.ManyToManyField(User, related_name='comment_likes')

    def total_likes(self):
        return self.likes.count()

    def liked_or_not(self):
        # if self.likes.filter(id=request.user.id).exists():
        #     liked = True
        # else:
        #     liked = False
        print("liked_or_not ran------------------")
        return "liked"

    def __str__(self):
        return "Comment on:-" + self.pin.image_name

    @property
    def children(self):
        print("hello this is model running----------------------------------------------")
        return Comment.objects.filter(parent=self).order_by('-creation_date').all()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False


class PinUser(models.Model):
    gender_type = (
        (1, "MALE"),
        (2, "FEMALE")
    )
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    user_image = CloudinaryField('image')
    email = models.CharField(max_length=200)
    gender = models.IntegerField(default=1, choices=gender_type, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    following_me = models.ManyToManyField(User, related_name='following_user')
    i_follows = models.ManyToManyField(User, related_name='i_follows')

    def __str__(self):
        return "Pin User:- " + self.name


@receiver(post_save, sender=User)
# Now Creating a Function which will automatically insert data in PinUser
def create_user_profile(sender, instance, created, **kwargs):
    # if Created is true (Means Data Inserted)
    print("signal running------", created, "----", instance.username)
    if created:
        print("inside creating")
        # PinUser.objects.create(
        #     user=instance,
        # )


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.pinuser.save()
