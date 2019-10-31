from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MangoAboutSerializer, UserSerializer, GroupSerializer
from .models import MangoAbout
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics
from django.contrib.auth.models import User, Group
# from dry_rest_permissions.generics import DRYPermissions


# Create your views here.


# Static views
def instruction(request):
    return render(request, 'Instructions.html')


def add_about(request):
    return render(request, 'about.html')


def search(request):
    return render(request, 'Index.html')


def addproject(request):
    return render(request, 'AddProject.html')


class MangoAboutViewSet(viewsets.ModelViewSet):
    queryset = MangoAbout.objects.all()
    serializer_class = MangoAboutSerializer
    filter_backends = (SearchFilter, OrderingFilter)
#    MangoAbout.owner = request.user
    search_fields = ['id', 'name', 'email', 'message', 'inserted_timestamp']


# try autorize
class ListMangoAbout(generics.ListCreateAPIView):
    queryset = MangoAbout.objects.all()
    serializer_class = MangoAboutSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['id', 'name', 'email', 'message', 'inserted_timestamp']


class DetailMangoAbout(generics.RetrieveUpdateDestroyAPIView):
    queryset = MangoAbout.objects.all()
    serializer_class = MangoAboutSerializer


# users
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
