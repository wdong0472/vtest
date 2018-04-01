# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


def dropdowntree(request):
    '''dropdown tree demo'''
    url = "qrik_demo/dropdowntree.html"
    return render(request,url)

