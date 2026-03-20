from django.urls import path
from . import views

urlpatterns = [
    path('', views.myIndex, name='index'), # 代表 myhello/ 之後不加東西就跑這個
    path('users', views.list_users, name='list_users'),
    path('courselist', views.list_courses, name='courselist'),
    path('addcourse', views.add_course, name='addcourse'),
    path('coursetable', views.course_table, name='course_table'),
]