from django.shortcuts import render, HttpResponse
from apps.basicweb.models import Major, Faculty
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
    objs = list(Major.objects.filter(Q(name__icontains=q_str)| Q(faculty__name__icontains=q_str))
                .values('id', 'name', 'faculty__name', 'faculty_id'))

    # 获取当前页的数据
    objs_one_page = objs[(page - 1) * limit: page * limit]
    # 定义一个返回值类型: code-状态， count-总数，用于分页 data-返回数据
    res = {'code': 0, 'count': len(objs), 'data': objs_one_page}
    return JsonResponse(res,safe=False,
                        json_dumps_params={'ensure_ascii': False})

def add_value(request):
    """添加专业"""
    # 获取传递过来的值
    faculty = request.POST.get('faculty')
    major = request.POST.get('major')
    # 写入数据库
    try:
        Major.objects.create(faculty_id=faculty, name=major)
        return JsonResponse({'status': True})
    except Exception as err:
        return JsonResponse({'status': False, 'error': '添加数据库写入异常,具体报错：' + str(err)})

def edit_value(request):
    """修改数据"""
    # 获取传递过来的值
    rec = request.POST
    try:
        # 后去当前的操作对象
        obj = Major.objects.filter(id=rec.get('major_id')).first()
        # 修改名称
        obj.name = rec.get('major')
        # 修改院系
        obj.faculty = Faculty.objects.filter(id=rec.get('faculty')).first()
        # 保存
        obj.save()
        # 返回
        return JsonResponse({'status': True})
    except Exception as err:
        return JsonResponse({'status': False, 'error': '修改数据出现异常,具体报错：' + str(err)})

def del_value(request):
    """删除"""
    # 接受传递的ID
    id = request.POST.get('id')

    # 实现删除功能
    # 写入数据库
    try:
        # 后去当前的操作对象
        obj = Major.objects.filter(id=id).first().delete()
        # 修改名称
        return JsonResponse({'status': True})
    except Exception as err:
        return JsonResponse({'status': False, 'error': '删除数据提交到数据库出现异常,具体报错：' + str(err)})

def query_value(request):
    """查询"""
    # 获取传递过来的值
    q_id = request.POST.get('id')
    try:
        # 获取数据
        objs = list(Major.objects.filter(faculty_id=q_id).values('id', 'name'))
        # 返回
        return JsonResponse({'status':True, 'data':objs})
    except Exception as err:
        return JsonResponse({'status': False, 'error':"获取专业的数据出现异常，具体异常：" + str(err)})



















