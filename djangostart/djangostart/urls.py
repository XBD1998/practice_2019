"""djangostart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from app1 import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^demo_form_db/$', views.demo_form_db),
    # url(r'^index/$', views.demo)
    url(r'^reg/$', views.reg),
    url(r'^login/$', views.reg),
    # url(r'^index/$', views.reg),
    url(r'^django_templates/', include('apps.django_templates.urls', namespace='django_templates')),

]
