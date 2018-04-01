from django.conf.urls import url, include
from qrik_test import views

urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^test_easyui_combotree/$',views.test_easyui_combotree,name='test_easyui_combotree'),
]
