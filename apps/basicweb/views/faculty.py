# ========= 引入模块 ============
from django.shortcuts import render, HttpResponse
# 引入数据库通用类
from utils import sqlhelper
# 引入JsonResponse
from django.http import JsonResponse
# 导入类
#from basicweb.models import Faculty

def index(request):
    return render(request, 'basic/faculty.html')

def list_values(request):
    # 接受查询条件
    q_str = request.POST.get('queryStr',"")

    # 准备SQL语句
    sql = """
    SELECT T3.Id,T3.Name, Count(*) As 'Number'
    FROM(
        SELECT T1.id, T1.Name 
        FROM Basic_Faculty AS T1
        INNER JOIN Basic_Major AS T2 ON T1.id = T2.faculty_id
        where T1.Name like '%s'
    ) As T3 
    GROUP BY T3.id,T3.Name
    """ % ('%' + q_str + '%')

    # 开始执行
    response = sqlhelper.get_db_data_dict(sql, ['id', 'name', 'number'])

    # 判断
    if response['status']:
        return JsonResponse({'status':True, 'data':response['data']})
    else:
        return JsonResponse({'status':False, 'error':response['error']})
