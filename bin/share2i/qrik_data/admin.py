# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import base_data
from .widgets import *
from qrik_libs import QrikBaseModel

# Register your models here.
class CategoryAdmin(QrikBaseModel.QrikBaseModelAdmin):
    pass

class CodeDataAdmin(admin.ModelAdmin):
    
    fields = ('qrik_creater', 'qrik_updater','qrik_code','qrik_name', 'qrik_value', 'category','qrik_order_no','qrik_enabled','qrik_summary')
    list_display = ('qrik_creater','category','qrik_code', 'qrik_name', 'qrik_value', 'qrik_order_no', 'qrik_stamp')
    list_filter = ('category', 'qrik_name','qrik_value')
    
class CodeManAdmin(admin.ModelAdmin):
    fields = ('qrik_creater', 'qrik_updater','qrik_code','qrik_name', 'qrik_value', 'qrik_order_no','qrik_enabled','qrik_summary')
    list_display = ('qrik_creater', 'qrik_code','qrik_name', 'qrik_value', 'qrik_order_no', 'qrik_stamp')
    list_filter = ('qrik_code','qrik_name')

   
admin.site.register(base_data.Category, CategoryAdmin)
admin.site.register(base_data.CodeData, CodeDataAdmin)
admin.site.register(base_data.CodeMan, CodeManAdmin)
