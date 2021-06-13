from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('create/', createUrl, name='index'),
    path('<str:pk>', go, name='go')
    
]
