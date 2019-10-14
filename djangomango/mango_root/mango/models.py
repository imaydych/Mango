from django.db import models

# Create your models here.


class MangoAbout (models.Model):
    name = models.TextField('Name', blank=True)
    email = models.TextField('Email', blank=True)
    message = models.TextField('Message', blank=True)


def __str__(self):
    return self.name


class Choice(models.Model):
    mangoabout = models.ForeignKey(MangoAbout, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)

    def __str__(self):
        return self.choice_text
