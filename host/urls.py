from django.urls import path, include
from . import  views
urlpatterns = [
    # 子路由配置，有对应的视图函数.
    path('', views.index, name='index'),
]