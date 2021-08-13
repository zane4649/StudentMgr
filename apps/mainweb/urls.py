from django.urls import path

# 引入当前app中的views
from mainweb import views as main_views

# 匹配当前App中的url
urlpatterns = [
    path('', main_views.index, name='main')
]