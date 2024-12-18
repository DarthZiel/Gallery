from django.urls import path
from .views import GetThreeDModels, GetThreeDModel, ShareGallery

urlpatterns = [
    path('3dmodels', GetThreeDModels.as_view()),
    path('3dmodel/<int:pk>', GetThreeDModel.as_view()),
    path('share/<str:username>', ShareGallery.as_view()),
]



