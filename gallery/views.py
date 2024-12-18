from rest_framework import generics
from rest_framework.filters import SearchFilter

from .serializers import ThreeDModelSerializer
from .models import ThreeDModel

class GetThreeDModels(generics.ListAPIView):
    serializer_class = ThreeDModelSerializer
    queryset = ThreeDModel.objects.all()

    filter_backends = [SearchFilter]  # Включаем поиск
    search_fields = ['name']  # Поля для поиска

class GetThreeDModel(generics.RetrieveAPIView):
    serializer_class = ThreeDModelSerializer
    queryset = ThreeDModel.objects.all()



