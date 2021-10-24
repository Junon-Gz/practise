from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound,Http404,JsonResponse
from demo.models import Users
from django.urls import reverse
from django.views import View
import datetime
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

    return render(request,"website/users/home.html")

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

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def failure(request):
    # 直接返回一个404,没有去加载404的模板页面
    # return HttpResponseNotFound('<h1>Page not found</h1>')

    # 可以直接返回一个status状态码
    # return HttpResponse(status=403)

    # 返回一个404的错误页面
    raise Http404("Poll does not exist")

def redire(request):
    # redirect重定向  reverse反向解析url地址
    return redirect(reverse('addusers'))

    # 执行一段js代码，用js进行重定向
    # return HttpResponse('<script>alert("添加成功");location.href = "/userindex"; </script>')

    # 加载一个提醒信息的跳转页面
    # context = {'info':'数据添加成功','u':'/userindex'}
    # return render(request,'info.html',context)

class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, views!')

def jsonrespon(request):
    data=[
        {"id":1,"name":"zhangsan","age":22,"gender":1},
        {"id":2,"name":"lisi","age":23,"gender":2},
        {"id":3,"name":"wangwu","age":26,"gender":1}
    ]
    return JsonResponse({"data":data})

def cookie(request):
    # 获取当前的 响应对象
    response = HttpResponse('cookie的设置')

    # 使用响应对象进行cookie的设置
    response.set_cookie('a','abc')
    
    m = request.COOKIES.get('a',None)
    if m:
        m = int(m)+1
    else:
        m = 1
    # 获取当前的 响应对象
    response = HttpResponse('cookie记录的计数器值：'+str(m))
    # 使用响应对象进行cookie的设置
    response.set_cookie('a',m)

    # 返回响应对象
    return response

def test_request(request):
    print("请求路径",request.path)
    print("请求方法",request.method)
    print("请求编码",request.encoding)
    print(request.GET.getlist('id'))
    print(request.GET.get('sex',None))
    return HttpResponse("测试请求对象")

def verifycode(request):
    #引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    #引入随机函数模块
    import random
    #定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(
        20, 100), 255)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象
    font = ImageFont.truetype('static/arial.ttf', 23)
    # font = ImageFont.load_default().font
    #构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    #释放画笔
    del draw
    #存入session，用于做进一步验证
    # request.session['verifycode'] = rand_str
    #内存文件操作
    """
    python2的为
    # 内存文件操作
    import cStringIO
    buf = cStringIO.StringIO()
    """
    # 内存文件操作-->此方法为python3的
    import io
    buf = io.BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')

def demo1(request):
    context={}
    context['name']='zhangsan'
    return render(request,'website/users/demo.html',context)