from django.urls import re_path as url
from EmployeeApp.views import EmployeeView


urlpatterns = [

    url(r'^emp/$', EmployeeView),
    url(r'^emp/([0-9]+)$', EmployeeView),
]
