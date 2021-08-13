from django.urls import path

#   引入当前app的views
from basicweb.views import faculty, major

# 匹配当前App中的url
urlpatterns = [
    # 院系管理
    path('faculty/', faculty.index, name='faculty'),
    path('faculty/list/', faculty.list_values, name='list_faculty'),

    # 专业管理
    path('major/', major.index, name='major'),
]