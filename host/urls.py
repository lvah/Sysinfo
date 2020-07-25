from django.urls import path, include
from . import  views
urlpatterns = [
    # 子路由配置，有对应的视图函数.
    path('', views.index, name='index'),
    path('disk/', views.disk, name='disk'),
    # 快速拷贝一行ctrl + d
    path('users/', views.users, name='users'),
]