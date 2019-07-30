from django.shortcuts import render,HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .forms import ContactForm, RegisterForm, LoginForm
from .models import UserInfo
# Create your views here.
def index(request):
    form = ContactForm()
    # form = ContactForm(request.GET)
    return render(request, "forms_base/index.html", {"form": form})

def register(request):
    #没有绑定数据的表单
    reg_form = RegisterForm()
    if request.method == "POST":
        #绑定数据的表单
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid():
            #is_valid => 用来验证表单中的所有数据中是否都合法
            #验证用户名：检查用户是否已经在数据中存在，可以对某个字段来验证
            #给某个字段添加验证方法：定义form的时候，clean_字段名
            #给整个表单添加验证方法：定义form的时候，加一个clean方法
            username = reg_form.cleaned_data["username"]
            password = reg_form.cleaned_data["password"]
            print("合法")
        else:
            print("不合法")
    return render(request, 'forms_base/register.html', {"form":reg_form})

def login(request):
    login_form = LoginForm()
    if request.method == "POST":
        login_form = LoginForm(request.POST)

def logout(request):
    print('退出成功')
    return HttpResponse("退出成功")

