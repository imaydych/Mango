from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class MangoAbout(models.Model):
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False,
    #                           null=True, blank=True, on_delete=models.CASCADE)
    name = models.TextField('Name', blank=True)
    email = models.TextField('Email', blank=True)
    message = models.TextField('Message', blank=True)
    inserted_timestamp = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


def __str__(self):
    return self.name
