# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import config

# Register your models here.
class ContextAdmin(admin.ModelAdmin):
    fields = ('qrik_creater', 'qrik_updater','qrik_code','qrik_name', 'qrik_value', 'template','qrik_order_no','qrik_enabled','qrik_summary')
    list_display = ('qrik_creater', 'qrik_code','qrik_name', 'qrik_value', 'template','qrik_stamp')
    list_filter = ('qrik_name',)

class ContextVarAdmin(admin.ModelAdmin):
    fields = ('context', 'qrik_code','qrik_name', 'qrik_value','qrik_order_no','qrik_enabled','qrik_summary')
    list_display = ('qrik_creater', 'qrik_code','qrik_name', 'qrik_value','qrik_stamp')
    list_filter = ('qrik_name','qrik_value')
   
admin.site.register(config.Context, ContextAdmin)
admin.site.register(config.ContextVar, ContextVarAdmin)




