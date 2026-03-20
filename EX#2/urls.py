from django.urls import path
from . import views

urlpatterns = [
    path('', views.myIndex, name='index'), # 代表 myhello/ 之後不加東西就跑這個
    path('users', views.list_users, name='list_users'),
]