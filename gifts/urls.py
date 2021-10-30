from django.urls import  path
from . import views 

urlpatterns = [
path('gifts/', views.index),
path('', views.index)
]