from django.urls import path
from . import views
from demo.views import MyView
urlpatterns = [
    path('', views.index,name="index"),
    #配置users信息操作路由
    path('users', views.indexUsers,name="indexusers"),
    path('users/add', views.addUsers,name="addusers"),
    path('users/insert', views.insertUsers,name="insertusers"),
    path('users/del/<int:uid>', views.delUsers,name="delusers"),
    path('users/edit/<int:uid>', views.editUsers,name="editusers"),
    path('users/update', views.updateUsers,name="updateusers"),
    path('users/current_datetime', views.current_datetime,name="current_datetime"),
    path('failure', views.failure,name="failure"),
    path('redire', views.redire,name="redire"),
    path('view', MyView.as_view(),name="view"),
    path('jsn', views.jsonrespon,name="jsn"),
    path('cookie', views.cookie,name="cookie"),
    path('test_request', views.test_request,name="test_request"),
    path('verifycode', views.verifycode,name="verifycode"),
    path('demo1', views.demo1,name="demo1")
]