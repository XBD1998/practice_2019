from django.shortcuts import render,HttpResponse
from .models import UserInfo
# Create your views here.
# def demo(request):
#     return render(request, 'base.html')
    # html = '<h1> I am a simply web</h1>'
    # return HttpResponse(html)

# def demo_form_db(request):
#     msg = ""
#     if request.method == "POST":
#         username = request.POST.get("email")
#         password = request.POST.get("password")
#         result = UserInfo.objects.get(email=username)
#         if result and result.password == password:
#             return HttpResponse(f"<h1>Welcome,{username}<h1>")
#         else:
#             msg = "用户名或密码错误"
#     kwgs = {
#         "msg":msg
#     }
#     return render(request, 'app1/demo01_form_db.html', kwgs)
def demo_form_db(request):
    msg = ""
    if request.method == "POST":  #浏览器中的为大写的POST故此处也要用大写的POST
        username = request.POST.get("email")
        password = request.POST.get("password")
        result = UserInfo.objects.get(email=username)
        if result and result.password == password:
            return HttpResponse(f"<h1>Welcome,{username}</h1>")
        else:
            msg = "用户名或密码错误"
        #     return render(request, 'app01/demo02_form2.html')

    kwgs = {
        "msg":msg
    }
    return render(request,'app1/demo01_form_db.html', kwgs)

def reg(request):
    print(request.method)
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        UserInfo.objects.create(username=username, password=password)
        # if username in user_list:
        #     print(f"<h1>Welcome,{username}</h1>")
        #     return render(request, 'app1/login.html')
        # else:
        #     msg = "请先注册"
        #     kwgs = {
        #         "msg":msg
        #     }
        #     return render(request, 'app1/reg.html', kwgs)
    return render(request, 'app1/reg.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_list = UserInfo.objects.all()
    return render(request, 'app1/login.html', )
def index(request):
    print(request.method)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_list = UserInfo.objects.all()
        user = {'username':username, 'password':password}
    return render(request, 'app1/index.html', {'user_list': user_list})


