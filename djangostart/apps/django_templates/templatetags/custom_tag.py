from django import template
#注册到template库里面
register = template.Library()

#自定义Tag
from django.conf import settings
@register.simple_tag
def mystatic(value):
    #STATIC_URL + value
    return settings.STATIC_URL + value