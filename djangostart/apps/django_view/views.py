from django.shortcuts import render,HttpResponse,Http404,get_object_or_404
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
# Create your views here.
def view_test(request):
    html = '<h1>I am Iron man</h1>'
    print(html)
    #此处不能 return html,必须返回一个HttpResponse对象
    return HttpResponse(html)
#
# def zoos(request, id):
#     if id > 100:
#         raise Http404('not exist')
#     return HttpResponse(f"这是第{id}个动物园的信息")

from app1.models import UserInfo
# from django.views.decorators.gizp import gzip_page
def zoos(request, id):
    id = int(id)
    #get_object_or_404 => 从Model中获取数据，如果没有获取到，就raise一个Http
    user = get_object_or_404(UserInfo, pk=id)
    return HttpResponse(user.username)

def index_404(request):
    #触发一个404错误
    raise Http404('not exist')
    return HttpResponse('I am index')

def userinfo(request):
    userlist = UserInfo.objects.all()
    title = "ABC"
    return render(request, "list_view.html", {"userlist":userlist, "title":title})
class MyTemplateView(TemplateView):
    template_name = "template_view.html"
    #设置模板解析后端引擎
    #template_engine

class MyListView(ListView):
    template_name = "list_view.html"
    context_object_name = "userlist"
    queryset = UserInfo.objects.filter(username="X_1")

    def get_queryset(self):
        return UserInfo.objects.filter(username="X_2")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "abc"
        return context

#
# class MyDetailView(DetailView):
#     model =UserInfo
#     template_name = "detail_view.html"
#
#     pk_url_kwarg = "user_id"
#
#     def get_onject(self, queryset=None):
#         user = super().get_object()
#         user.abc = "hello"
#         return user






