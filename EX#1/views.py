from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_api(request):
    # 取得參數 name，若無則預設為 CGU
    name = request.query_params.get('name', 'CGU')
    return Response(f"Hello {name}")