from django.urls import path
from .views import GetThreeDModels, GetThreeDModel

urlpatterns = [
    path('3dmodels', GetThreeDModels.as_view()),
    path('3dmodel/<int:pk>', GetThreeDModel.as_view()),
]



