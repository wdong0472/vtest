# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib.admin import site
from django.shortcuts import render
from django.db import models
from django.http import HttpRequest, HttpResponseRedirect,Http404
from django.template import RequestContext
from django.contrib.auth import authenticate,login as aulogin,logout as aulogout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission,User

import pymongo
from pymongo import MongoClient

import json
from bson import json_util as jsonb    
import re
    
from .models import *
from qrik_auth.models import App, Menu

def index(request):
    url = 'qrik_ui/index.html' 
    return render(request, url)


def myurls(request):
    '''系统主页:用户登录后导航至此'''
    url = 'qrik_ui/myurls.html'
    
    client = MongoClient('share2i.com',27017)    
    db = client.admin
    db.authenticate("root", "root")
    myurls = db.myurls
    
    user = request.GET.get('u')
    category = request.GET.get('c')
    search = request.GET.get('s')
    page_no = request.GET.get('p')
    
    #判断条件是否有效，无效则给出默认值
    if not user:
        user_pattern = re.compile("\w*")
    else:
        user_pattern = re.compile("\w*%s\w*" % user)
        
    if not category:
        category = "全部"
        category_pattern = re.compile("\w*")
    else:
        category_pattern = re.compile("\w*%s\w*" % category)        
    
    if not search:
        search = ""
        search_pattern = re.compile("\w*")
    else:
        search_pattern = re.compile("\w*%s\w*" % search)        
        
    if not page_no:
        page_no = 1
    
    #query = {"user":user_pattern, "category":category_pattern, "$or":[{"title":search_pattern}, {"url":search_pattern}]}
    
    query = {"$or":[{"title":search_pattern}, {"url":search_pattern}]}
    page = int(page_no)
    pagesize=10
    pos = ( page - 1 ) * pagesize
    count =range(1,int(myurls.count() / 10) + 2)
    rows = myurls.find(query).sort([("stamp", pymongo.DESCENDING)]).skip(pos).limit(pagesize)
    
    #上一页
    prev_page = page - 1
    
    #下一页
    next_page = page + 1
    
    return render(request,url, {"data":jsonb.dumps(list(rows)),'category':category, 'search':search, 'count':count,'cur_page':page, 'prev_page':prev_page,'next_page':next_page})


def mybookmarks(request):
    '''系统主页:用户登录后导航至此'''
    url = 'qrik_ui/mybookmarks.html'
    
    client = MongoClient('share2i.com',27017)    
    db = client.admin
    db.authenticate("root", "root")
    myurls = db.myurls
    
    user = request.GET.get('u')
    category = request.GET.get('c')
    search = request.GET.get('s')
    page_no = request.GET.get('p')
    
    #判断条件是否有效，无效则给出默认值
    if not user:
        user_pattern = re.compile("\w*")
    else:
        user_pattern = re.compile("\w*%s\w*" % user)
        
    if not category:
        category = "全部"
        category_pattern = re.compile("\w*")
    else:
        category_pattern = re.compile("\w*%s\w*" % category)        
    
    if not search:
        search = ""
        search_pattern = re.compile("\w*")
    else:
        search_pattern = re.compile("\w*%s\w*" % search)        
        
    if not page_no:
        page_no = 1
    
    #query = {"user":user_pattern, "category":category_pattern, "$or":[{"title":search_pattern}, {"url":search_pattern}]}
    
    query = {"$or":[{"title":search_pattern}, {"url":search_pattern}]}
    page = int(page_no)
    pagesize=10
    pos = ( page - 1 ) * pagesize
    count =range(1,int(myurls.count() / 10) + 2)
    rows = myurls.find(query).sort([("stamp", pymongo.DESCENDING)]).skip(pos).limit(pagesize)
    
    #上一页
    prev_page = page - 1
    
    #下一页
    next_page = page + 1
    
    return render(request,url, {"data":jsonb.dumps(list(rows)),'category':category, 'search':search,     'count':count,'cur_page':page, 'prev_page':prev_page,'next_page':next_page})

def login(request):
    '''登录:如果用户已经登录则直接导航到主页面'''
    if request.user.is_authenticated:
        return main(request)
    
    url = 'qrik_ui/login.html'
    return render(request,url)

@login_required(login_url='/qrik_ui/login/')


def logout(request):
    '''注销:注销成功后导航至登录界面'''
    aulogout(request)
    return login(request)
    

def login_post(request):
    '''登录处理:用户点击登录按钮后的处理逻辑'''
    name=request.POST.get('form-username',default=None)
    pwd=request.POST.get('form-password',default=None)
    
    #认证用户,认证成功则进行登录处理否则提示用户相应的错误信息
    user=authenticate(username=name,password=pwd)
    
    if user is not None:        
        aulogin(request,user)
        return HttpResponseRedirect('/qrik_ui/main/')
       
    else:
        url = 'qrik_ui/login.html'   
        return render(request, url,{
                'error': '用户名或者密码不正确',
                'form-username': name,
                'form-password': pwd,
            })

@login_required(login_url='/qrik_ui/login/')
def main(request):
    '''系统主页:用户登录后导航至此,否则导航至登录界面'''
    url = 'qrik_ui/main.html'
    
    groups = request.user.groups.all()
    
    apps = {}
    menus = {}
    
    for group in groups:
        for menu in group.menu_set.all():
            if menus.has_key(menu.qrik_key):
                pass
            else:
                menus[menu.qrik_key] = menu   
         
            if apps.has_key(menu.app.qrik_key):
                pass
            else:
                apps[menu.app.qrik_key] = menu.app               
                
                
    return render(request,url,{'apps':apps.values, 'menus':menus.values})
