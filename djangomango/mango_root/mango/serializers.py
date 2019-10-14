from rest_framework import serializers
from .models import MangoAbout


class MangoAboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = MangoAbout
        fields = ('name', 'email', 'message')
