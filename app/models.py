from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.
class Folder(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ImagesPin(models.Model):
    image = CloudinaryField('image')
    image_name = models.CharField(max_length=200)
    tags = models.TextField()

    def __str__(self):
        return self.image_name


class UserImage(models.Model):
    imagesPin = models.ForeignKey(ImagesPin, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)

    def __str__(self):
        return self.folder.name
