from rest_framework.serializers import ModelSerializer
from .models import ThreeDModel
from djoser.serializers import UserCreateSerializer
from django.contrib.auth.models import Group

class ThreeDModelSerializer(ModelSerializer):
    class Meta:
        model = ThreeDModel
        fields = '__all__'
class CustomUserCreateSerializer(UserCreateSerializer):
    def create(self, validated_data):
        user = super().create(validated_data)
        group, _ = Group.objects.get_or_create(name='gallery')
        user.groups.add(group)
        user.is_staff = True
        user.save()
        return user