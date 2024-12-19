from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from .serializers import ThreeDModelSerializer
from .models import ThreeDModel


class GetThreeDModels(generics.ListAPIView):
    serializer_class = ThreeDModelSerializer
    queryset = ThreeDModel.objects.all()
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]  # Включаем поиск
    search_fields = ['name']  # Поля для поиска

    def get_queryset(self):
        return ThreeDModel.objects.filter(user=self.request.user)


class GetThreeDModel(generics.RetrieveAPIView):
    serializer_class = ThreeDModelSerializer
    queryset = ThreeDModel.objects.all()


class ShareGallery(generics.ListAPIView):
    serializer_class = ThreeDModelSerializer
    queryset = ThreeDModel.objects.all()
    lookup_field = 'username'
