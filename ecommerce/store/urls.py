from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('type/<str:slug>',type,name='type'),
]