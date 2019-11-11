from django.db import models


# Create your models here.


class AddProject(models.Model):
    owner = models.ForeignKey('auth.User', related_name='MangoAbouts',
                              on_delete=models.CASCADE)  # Link owner field with users from User model
    name = models.TextField('Name', blank=True)
    start = models.DateField('Start Date', blank=True)
    end = models.DateField('End Date', blank=True)
    category = models.TextField('Category', blank=True)
    description = models.TextField('Description', blank=True)
    resources = models.TextField('Resources', blank=True)
    contributors = models.TextField('Contributors', blank=True)
    inserted_timestamp = models.DateTimeField(auto_now_add=True)  # auto-add timestamp
    objects = models.Manager()


def __str__(self):
    return self.name
