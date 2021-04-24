from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>', special_info)
]
