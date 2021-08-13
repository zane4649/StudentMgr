from django.contrib import admin
from django.urls import path

# 引入include
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),

    # 基础页面
    path('basic/', include('basicweb.urls')),

    # 核心页面
    path('main/', include('mainweb.urls')),

    # 学生信息
    path('student/', include('studentweb.urls'))
]
