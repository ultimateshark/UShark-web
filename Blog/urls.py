from .views import *
from django.urls import path,include
urlpatterns = [
    path('',Home),
    path('blog/<str:blog>',Blog)
]