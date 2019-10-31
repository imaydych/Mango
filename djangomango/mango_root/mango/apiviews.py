from rest_framework import viewsets, serializers
from django.http import JsonResponse
from .serializers import MangoAboutSerializer
from .models import MangoAbout



# class MangoAboutViewSet(viewsets.ModelViewSet):
#     queryset = MangoAbout.objects.all()
#     serializer_class = MangoAboutSerializer


# class about_list(APIView):
#     def get(self, request):
#         mangoabout = MangoAbout.name.all()[:20]
#         data = MangoAboutSerializer(MangoAbout, many=True).data
#         return Response(data)
#
#
# class about_detail(APIView):
#     def get(self, request, pk):
#         mangoabout = get_object_or_404(MangoAbout, pk=pk)
#         data = MangoAboutSerializer(MangoAbout).data
#         return Response(data)
