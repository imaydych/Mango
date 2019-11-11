from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import AddProject


class AddProjectSerializer(serializers.ModelSerializer):
    # Display the owner's username (read-only)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = AddProject
        fields = ('id', 'owner', 'name', 'start', 'end', 'category', 'description', 'resources', 'contributors', 'inserted_timestamp')


class UserAddProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AddProject
        fields = ('name',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    AddProjects = UserAddProjectSerializer(
        many=True,
        read_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


