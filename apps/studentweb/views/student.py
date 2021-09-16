from django.shortcuts import render
from apps.studentweb.models import Student
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'student/student.html')

def list_values(request):
    """获取数据"""
    # 获取分页的page和limit
    page = int(request.POST.get('page',0))
    limit = int(request.POST.get('limit', 0))

    # 查询的条件获取
    q_sno_name = request.POST.get('q_sno_name')
    q_faculty = request.POST.get('q_faculty')
    q_major = request.POST.get('q_major')
    q_status = request.POST.get('q_status')

    # 获取学生信息
    # objs = list(Student.objects.all().values('sno', 'name', 'gender', 'birthday', 'mobile', 'email', 'address'
    #                                     , 'major__name', 'faculty__name', 'start_date', 'status'))


    # 第一次过滤: 模糊查询学号 或 姓名
    filter_data = Student.objects.filter(Q(sno__icontains=q_sno_name)| Q(name__icontains=q_sno_name))

    # 第二次过滤：匹配院系信息
    if len(q_faculty) > 0:
        filter_data = filter_data.filter(faculty_id = q_faculty)

    # 第三次过滤：匹配专业信息
    if len(q_major) > 0:
        filter_data = filter_data.filter(major_id=q_major)

    # 第四次过滤：匹配学生的状态
    if q_status == 'true':
        filter_data = filter_data.filter(status__icontains='在校')

    # 处理数据：list -- values
    objs = list(filter_data.values('sno', 'name', 'gender', 'birthday', 'mobile', 'email', 'address'
                                         , 'major__name', 'faculty__name', 'start_date', 'status'))

    # 定义一个返回的数据集
    res = {'code': 0, 'count': len(objs), 'data': objs}

    # 判断是否接收到page和limit
    if page != 0 and limit != 0:
        on_page_data = objs[(page-1) * limit: page * limit]
        res['data'] = on_page_data

    # 返回
    return JsonResponse(res)



















