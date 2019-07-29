from django.shortcuts import render

# Create your views here.

def index(request):
    kwgs = {
        "project_name":"超级项目",
        "project_info1":["超级项目1","This is a super project"],
        "project_info2":{"name":"super project_2", "desc":"This is super project 2"},
        "good_students":[{"name":"jack","hobby":"basketball","src":"/static/悟空.jpg"},
                         {"name":"Derrick","hobby":"basketball","src":"/static/七龙珠.jpg"},
                         {"name":"Derrick_2","hobby":"volleyball","src":"/static/龙珠一.jpg"},
                         {"name":"Derrick_3","hobby":"tennis","src":"/static/悟空.jpg"},
        ],
    }
    return render(request, "django_templates/index.html", kwgs)
