from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework import viewsets
from .forms import AboutForm
from django.http import JsonResponse
from .models import MangoAbout


# Create your views here.


def add_about(request):
    submitted = False
    if request.method == 'POST':
        form = AboutForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/about/?submitted=True')
    else:
        form = AboutForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'about.html',
        {'form': form, 'thank you for submittin our form': submitted})


def instruction(request):
    return render(request, 'Instructions.html')


def search(request):
    return render(request, 'Index.html')


def addproject(request):
    return render(request, 'AddProject.html')


# class MangoViewSet(viewsets.ModelViewSet):
#     queryset = MangoAbout.objects.all()

# def about_list(request):
#     MAX_OBJECTS = 20
#     mango = MangoAbout.objects.all()[:MAX_OBJECTS]
#     data = {"results": list(MangoAbout.values("name", "email", "message"))}
#     return JsonResponse(data)
#
#
# def about_detail(request, pk):
#     mango = get_object_or_404(MangoAbout, pk=pk)
#     data = {"results": {
#         "email": MangoAbout.name,
#         "message": MangoAbout.message,
#     }}
#     return JsonResponse(data)
