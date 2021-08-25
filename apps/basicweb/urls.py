from django.urls import path

# 引入当前app的views
from basicweb.views import faculty, major

# 匹配当前App中的url
urlpatterns = [
    # ============ 院系管理 =========
    path('faculty/', faculty.index, name="faculty"),  # 展示前端页面
    path('faculty/list/', faculty.list_values, name="list_faculty"),  # 获取数据
    path('faculty/add/', faculty.add_value, name='add_faculty'),    #添加数据
    path('faculty/edit/', faculty.edit_value, name='edit_faculty'), #修改数据
    path('faculty/del/', faculty.del_value, name='del_faculty'), # 删除数据

    # 专业管理
    path('major/', major.index, name='major'),
    path('major/list/', major.list_values, name='list_major'),
]


