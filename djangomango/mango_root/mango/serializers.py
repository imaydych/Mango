from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import MangoAbout


class MangoAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = MangoAbout
        fields = ('id', 'name', 'email', 'message', 'inserted_timestamp', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


