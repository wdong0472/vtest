# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from qrik_tools.models.config import Context

# Create your views here.

# @login_required(login_url='/qrik_ui/login/')
def easyui_combotree(request, code, id):
    url = 'qrik_widgets/easyui_combotree.html'
    #context = Context.objects.filter(code=code)
    # if context is None:
        # return ""
    # context.url = context.ContextVar_set.filter(code='url')
    
    return render(request,url,{'context':None, 'id':id})
    
