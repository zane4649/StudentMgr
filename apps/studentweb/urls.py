from django.urls import path

# 引入当前app中的views
from apps.studentweb.views import student as student_views

# 匹配当前App中的url
urlpatterns = [
    path('', student_views.index, name='student'),
    path('list/', student_views.list_values, name='list_student'),
]