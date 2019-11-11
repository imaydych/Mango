from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import AddProjectSerializer, UserSerializer, GroupSerializer
from .models import AddProject
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics
from django.contrib.auth.models import User, Group
from . import custompermission


# Create your views here.


# Static views - links to page html templates
def instruction(request):
    return render(request, 'Instructions.html')


def add_about(request):
    return render(request, 'about.html')


def search(request):
    return render(request, 'Index.html')


def addproject(request):
    return render(request, 'AddProject.html')


# API views
class ListAddProject(generics.ListCreateAPIView):
    # View all objects from the table
    queryset = AddProject.objects.all()
    serializer_class = AddProjectSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['id', 'name', 'start', 'end', 'category', 'description',
                     'resources', 'contributors', 'inserted_timestamp']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    permission_classes = (
        permissions.IsAuthenticated,
        custompermission.IsCurrentUserOwner,
    )


class DetailAddProject(generics.RetrieveUpdateDestroyAPIView):
    # Check one object from the table, update, delete it
    queryset = AddProject.objects.all()
    serializer_class = AddProjectSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        custompermission.IsCurrentUserOwner,
    )


# Users
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
