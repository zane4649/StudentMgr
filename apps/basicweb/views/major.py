from django.shortcuts import render, HttpResponse
from apps.basicweb.models import Major
from django.http import JsonResponse

def index(request):
    return render(request, 'basic/major.html')

def list_values(request):
    """获取数据"""
    # 获取所有的数据
    objs = list(Major.objects.all().values('id', 'name', 'faculty__name'))

    # 定义一个返回值类型
    res = {'code':0, 'data':objs}
    return JsonResponse(res)

