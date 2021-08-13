from django.urls import path

# 引入当前app中的views
from studentweb import views as student_views

# 匹配当前App中的url
urlpatterns = [
    path('', student_views.index, name='student')
]