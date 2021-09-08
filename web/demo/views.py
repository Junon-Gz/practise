from django.shortcuts import render
from django.http import HttpResponse
from demo.models import Users
# Create your views here.
def index(request):
    #执行Model的操作

    #添加数据
    # ob = Users() #实例化一个新对象(空对象)
    # ob.name = '张四'
    # ob.age = 22
    # ob.phone = '12345'
    # ob.save() #新对象是添加操作，已存在对象则是修改

    #删除数据
    # mod = Users.objects #获取users的model对象
    # users = mod.get(id=3)
    # print(users.name)
    # users.delete()#执行删除

    #修改操作
    # ob = Users.objects.get(id=2)
    # print(ob.name)
    # ob.name = '小刘'
    # ob.age = 26
    # ob.save()

    #数据查询
    # mod = Users.objects #获取Users模型的Model操作对象
    # ulist = mod.filter(age__gt=25) #获取所有age>25的数据
    # ulist = mod.filter(age__gte=25) #获取所有age>=25的数据
    # ulist = mod.filter(age__lte=25) #获取所有age<=25的数据
    # ulist = mod.order_by('age') #获取所有age<=25的数据

    # for u in ulist:
    #     print(u.id,u.name,u.age,u.phone,u.addtime)

    return HttpResponse("首页 <br/> <a href='/users'>用户管理信息</a>")

#浏览用户信息
def indexUsers(request):
    try:
        ulist = Users.objects.all()
        context = {"userlist":ulist}
        return render(request,"website/users/index.html",context) #加载模板
    except:
        return HttpResponse("没有找到用户信息")
#加载添加用户信息表单
def addUsers(request):
    return render(request,"website/users/add.html")
#执行用户信息添加
def insertUsers(request):
    try:
        ob = Users()
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.phone = request.POST['phone']
        ob.save()
        context = {"info":"添加成功"}
    except:
        context = {"info":"添加失败"}
    return render(request,"website/users/info.html",context)

#执行用户信息删除
def editUsers(request,uid=0):
    try:
        ob = Users.objects.get(id=uid)
        context = {"user":ob}
        return render(request,"website/users/edit.html",context)
    except:
        context = {"info":"没有找到要修改的数据"}
        return render(request,"website/users/info.html",context)

#加载用户信息修改表单
def delUsers(request,uid=0):
    try:
        ob = Users.objects.get(id=uid)
        ob.delete()
        context = {"info":"删除成功"}
    except:
        context = {"info":"删除失败"}
    return render(request,"website/users/info.html",context)
#执行用户信息修改
def updateUsers(request):
    try:
        uid = request.POST['id']#获取要修改数据的id号
        ob = Users.objects.get(id=uid)
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.phone = request.POST['phone']
        ob.save()
        context = {"info":"修改成功"}
    except:
        context = {"info":"修改失败"}
    return render(request,"website/users/info.html",context)