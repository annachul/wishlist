from django.urls import  path
from . import views 

urlpatterns = [
path('gifts/', views.index, name='all_gifts'),
path('', views.index, name='all_gifts'),
path('gifts/<id>', views.giftdetail, name="gift_detail")
]