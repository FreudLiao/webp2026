from django.urls import path
from . import views

urlpatterns = [
    # 配合投影片網址，路徑設為 myhello/
    path('myhello/', views.hello_api),
]