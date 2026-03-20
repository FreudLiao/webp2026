# --- 1. 基礎工具匯入 ---
import logging
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# --- 2. Django REST Framework 工具匯入 ---
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# --- 3. 匯入你自己在 models.py 寫的倉庫資料表 ---
# 這裡最重要，如果不匯入，電腦就不認識 User 和 Post
from .models import User, Post 

# --- 4. 設定日誌「眼睛」 ---
logger = logging.getLogger('django')

# --- 5. 邏輯實作：首頁 API ---
@api_view(['GET'])
def myIndex(request):
    logger.info("有人存取了首頁 API")
    return Response({"data": "Hello CGU! 首頁運作正常"})

# --- 6. 邏輯實作：使用者列表 API (含分頁) ---
@api_view(['GET'])
def list_users(request):
    # 取得網址參數中的頁碼 ?page=1，沒傳的話預設是 1
    page_number = request.GET.get('page', 1)
    
    # 從資料庫抓出所有使用者資料
    users_queryset = User.objects.all().values()
    
    # 設定分頁：每頁只顯示 10 筆 (對應投影片第 45 頁)
    paginator = Paginator(users_queryset, 10)
    
    try:
        users_page = paginator.page(page_number)
    except PageNotAnInteger:
        # 如果使用者亂輸入(例如字母)，給他第一頁
        users_page = paginator.page(1)
    except EmptyPage:
        # 如果輸入的頁數超出範圍，給他最後一頁
        users_page = paginator.page(paginator.num_pages)
    
    logger.debug(f"讀取使用者列表 - 第 {page_number} 頁")
    
    # safe=False 是因為 list 不是字典格式，這是 JsonResponse 的規定
    return JsonResponse(list(users_page), safe=False)