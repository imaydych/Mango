from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import MangoAbout, Choice
from .serializers import MangoAboutSerializer


class about_list(APIView):
    def get(self, request):
        mangoabout = MangoAbout.name.all()[:20]
        data = MangoAboutSerializer(MangoAbout, many=True).data
        return Response(data)


class about_detail(APIView):
    def get(self, request, pk):
        mangoabout = get_object_or_404(MangoAbout, pk=pk)
        data = MangoAboutSerializer(MangoAbout).data
        return Response(data)
