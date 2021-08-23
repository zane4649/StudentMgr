# ========= 引入模块 ============
from django.shortcuts import render, HttpResponse
# 引入数据库通用类
from utils import sqlhelper
# 引入JsonResponse
from django.http import JsonResponse
# 导入类
from apps.basicweb.models import Faculty

def index(request):
    return render(request, 'basic/faculty.html')

def list_values(request):
    # 接受查询条件
    q_str = request.POST.get('queryStr',"")

    # 准备SQL语句
    sql = """
        Select T3.Id,T3.Name, Count(T3.id2) As 'Number' 
        From 
        (
            Select T1.Id, T1.Name, T2.Id As "id2"
            from Basic_Faculty As T1
            Left Join Basic_Major As T2 On T1.id = T2.faculty_id
    			  where T1.Name Like '%s'
        ) AS T3
        Group By T3.Id,T3.Name
        """ % ('%' + q_str + '%')

    # 开始执行
    response = sqlhelper.get_db_data_dict(sql, ['id', 'name', 'number'])

    # 判断
    if response['status']:
        return JsonResponse({'status': True, 'data': response['data']})
    else:
        return JsonResponse({'status': False, 'error': response['error']})

def add_value(request):
    '''添加'''
    # 接收传递的名称
    name = request.POST.get('name')
    try:
        # 写入数据库
        Faculty.objects.create(name=name)
        return JsonResponse({'status': True})
    except Exception as err:
        return JsonResponse({'status': False, 'error':'写入数据库失败:' + str(err)})

def edit_value(request):
    """修改"""
    # 获取传递过来的数据
    id = request.POST.get('id','')
    name = request.POST.get('name','')
    try:
        obj = Faculty.objects.get(id=id)
        obj.name = name
        obj.save()
        return JsonResponse({'status': True})
    except Exception as err:
        return JsonResponse({'status': False, 'error': '修改数据库出现异常: ' + str(err)})

def del_value(request):
    """删除"""
    id = request.POST.get('id')
    try:
        Faculty.objects.get(id=id).delete()
        return JsonResponse({'status': True})
    except Exception as err:
        return JsonResponse({'status': False, 'error': '提交数据到数据库出现异常,原因:' + str(err)})







