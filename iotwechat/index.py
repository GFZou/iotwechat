from django.http import HttpResponse


def index(request):
    return HttpResponse("欢迎来到智联云控数据后台，您可以在网址后面加入：sqladmin进入数据管理界面! ")
