from django.db import models
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect


class MangoAbout (models.Model):
    name = models.TextField('Name', blank=True)
    email = models.TextField('Email', blank=True)
    message = models.TextField('Message', blank=True)


def About(request):
    submitted = False
    if request.method == 'POST':
        form = MangoAbout(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/about?submitted=True')
        else:
            form = MangoAbout()
            if 'submitted' in request.GET:
                submitted = True
    return render(request, '/mango_site/static/pages/about.html', {'form': form, 'submitted': submitted})
