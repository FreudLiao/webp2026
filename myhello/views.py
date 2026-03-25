import logging
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, Post, Course
from django.shortcuts import render

logger = logging.getLogger('django')

# --- 5. 邏輯實作：首頁 API ---
@api_view(['GET'])
def myIndex(request):
    logger.info("有人存取了首頁 API")
    return Response({"data": "Hello CGU! 首頁運作正常"})

# --- 6. 邏輯實作：使用者列表 API (含分頁) ---
@api_view(['GET'])
def list_users(request):
    page_number = request.GET.get('page', 1)
    users_queryset = User.objects.all().values()
    paginator = Paginator(users_queryset, 10)
    
    try:
        users_page = paginator.page(page_number)
    except PageNotAnInteger:
        users_page = paginator.page(1)
    except EmptyPage:
        users_page = paginator.page(paginator.num_pages)
        
    # 同樣在這裡加上編址設定[cite: 1, 2]
    return JsonResponse(list(users_page), safe=False, json_dumps_params={'ensure_ascii': False})

@api_view(['GET'])
def list_courses(request):
    data = Course.objects.all().values()
    # 增加 json_dumps_params 參數，強制關閉 ASCII 編碼
    return JsonResponse(list(data), safe=False, json_dumps_params={'ensure_ascii': False})

# 2. 加入課程 API (對應投影片 /addcourse)
@api_view(['GET'])
def add_course(request):
    dept = request.GET.get('Department')
    title = request.GET.get('CourseTitle')
    teacher = request.GET.get('Instructor')
    
    if dept and title and teacher:
        Course.objects.create(Department=dept, CourseTitle=title, Instructor=teacher)
        return Response({"message": f"課程 {title} 已成功加入！"})
    return Response({"error": "請提供完整的 Department, CourseTitle 與 Instructor 參數"}, status=400)

@api_view(['GET'])
def course_table(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})