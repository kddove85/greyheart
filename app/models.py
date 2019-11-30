from django.db import models
from django.db.models import ImageField
import os


def get_image_path(instance, filename):
    pass


def get_greyhound_image_path(instance, filename):
    return os.path.join('greyhounds', filename)


def get_board_member_image_path(instance, filename):
    return os.path.join('boardmembers', filename)


# Create your models here.
class Greyhound(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    is_spotlight = models.BooleanField(default=False)
    profile_image = ImageField(upload_to=get_greyhound_image_path, blank=True, null=True)


class BoardMember(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    bio = models.TextField()
    profile_image = ImageField(upload_to=get_board_member_image_path, blank=True, null=True)


class Event(models.Model):
    pass


class Tribute(models.Model):
    pass
