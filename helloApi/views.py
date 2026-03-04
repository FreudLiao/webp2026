from django.http import HttpResponse # 這次改用 HttpResponse 回傳純文字
import django

def hello_api(request):
    # 1. 從網址取得 'name' 參數的內容
    # 如果網址沒給參數，預設顯示 'CGU' (像投影片那樣)
    user_name = request.GET.get('name', 'CGU')
    
    # 2. 組合字串
    result_text = f"Hello {user_name}"
    
    # 3. 回傳純文字給瀏覽器
    return HttpResponse(result_text)