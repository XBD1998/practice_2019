from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^view_test/$', views.view_test, name="view_test"),
    url(r'^zoo/(\d+)/', views.zoos, name="zoos"),
    url(r'^index_404/$', views.index_404, name="index_404"),
    url(r'^templateview/$', views.MyTemplateView.as_view(), name="templateview"),
    url(r'^listview/$', views.MyListView.as_view(), name="listview")
]