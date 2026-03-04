from django.urls import path
from . import views

urlpatterns = [
    # 將路徑改為 myhello/ 
    path('myhello/', views.hello_api),
]