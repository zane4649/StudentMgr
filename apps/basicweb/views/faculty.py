from django.shortcuts import render, HttpResponse
from utils import sqlhelper
from django.http import JsonResponse

def index(request):
    return render(request, 'basic/faculty.html')

def list_values(request):
    q_str = request.POST.get('queryStr', ' ')
    sql = """
    SELECT T3.Id,T3.Name, COUNT(*) AS 'Number'
    FROM(
        SELECT T1.id, T1.Name 
        FROM Basic_Faculty AS T1
        INNER JOIN Basic_Major AS T2 ON T1.id = T2.faculty_id
        where T1.Name Like '%s'
    ) as T3 
    GROUP BY T3.id,T3.Name
    """ % ('%' + q_str + '%')

#
    response = sqlhelper.get_db_data_dict(sql,['id', 'name', 'number'])
    if response['status']:
        return JsonResponse({'status':True, 'data':response['data']})
    else:
        return JsonResponse({'status':False, 'error':response['error']})
