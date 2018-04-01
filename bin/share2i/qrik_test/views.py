# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    text = 'hello,world'
    return HttpResponse(text)

def test_easyui_combotree(request):
    url = 'qrik_test/test_easyui_combotree.html'
    return render(request, url)


    
