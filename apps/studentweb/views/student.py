from django.shortcuts import render
from apps.studentweb.models import Student
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'student/student.html')

def list_values(request):
    """获取数据"""
    # 获取分页的page和limit
    page = int(request.POST.get('page',0))
    limit = int(request.POST.get('limit', 0))

    # 获取学生信息
    objs = list(Student.objects.all().values('sno', 'name', 'gender', 'birthday', 'mobile', 'email', 'address'
                                        , 'major__name', 'faculty__name', 'start_date', 'status'))

    # 定义一个返回的数据集
    res = {'code': 0, 'count': len(objs), 'data': objs}

    # 判断是否接收到page和limit
    if page != 0 and limit != 0:
        on_page_data = objs[(page-1) * limit: page * limit]
        res['data'] = on_page_data

    # 返回
    return JsonResponse(res)



















