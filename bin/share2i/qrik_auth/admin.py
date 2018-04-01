# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import *

class AppAdmin(admin.ModelAdmin):
    fields = ('qrik_creater', 'qrik_updater','qrik_code','qrik_name', 'qrik_value','qrik_order_no','qrik_enabled','qrik_summary')
    list_display = ('qrik_creater', 'qrik_code','qrik_name','qrik_stamp')
    list_filter = ('qrik_name',)


class MenuAdmin(admin.ModelAdmin):
    fields = ('qrik_creater', 'qrik_updater','qrik_code','qrik_name','app','groups','qrik_value','qrik_order_no','qrik_enabled','qrik_summary')
    list_display = ('qrik_creater', 'qrik_code','qrik_name','app','qrik_stamp')
    list_filter = ('qrik_name',)

class ActionAdmin(admin.ModelAdmin):
    fields = ('qrik_creater', 'qrik_updater','qrik_code','qrik_name','menu','qrik_value','qrik_order_no','qrik_enabled','qrik_summary')
    list_display = ('qrik_creater', 'qrik_code','qrik_name','menu','qrik_stamp')
    list_filter = ('qrik_name',)
    
admin.site.register(App, AppAdmin) 
admin.site.register(Menu, MenuAdmin) 
admin.site.register(Action, ActionAdmin) 


