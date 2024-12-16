from rest_framework.serializers import ModelSerializer
from .models import ThreeDModel


class ThreeDModelSerializer(ModelSerializer):
    class Meta:
        model = ThreeDModel
        fields = '__all__'
