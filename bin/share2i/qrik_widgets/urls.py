from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^easyui_combotree/(?P<code>\w+)/(?P<id>\w+)/$', views.easyui_combotree, name="easyui_combotree"),
]
