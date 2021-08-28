from django.shortcuts import render, HttpResponse
from apps.basicweb.models import Major
from django.http import JsonResponse
from django.db.models import Q


def index(request):
    return render(request, 'basic/major.html')

def list_values(request):
    """获取数据"""
    # 获取传递过来的2个参数
    page = int(request.POST.get('page', 0))
    limit = int(request.POST.get('limit', 0))
    q_str = request.POST.get('inputStr', '')

    # 获取所有的数据
    objs = list(Major.objects.filter(Q(name__icontains=q_str)| Q(faculty__name__icontains=q_str)).values('id', 'name', 'faculty__name'))

    # 获取当前页的数据
    objs_one_page = objs[(page - 1) * limit: page * limit]
    # 定义一个返回值类型: code-状态， count-总数，用于分页 data-返回数据
    res = {'code': 0, 'count': len(objs), 'data': objs_one_page}
    return JsonResponse(res)











