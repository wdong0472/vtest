# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth.models import User, Group
from django.db import models
from qrik_libs.QrikBaseModel import QrikBaseModel, modify_fields, AbstractParentClass


@modify_fields(qrik_code={'verbose_name':'功能编码'}, qrik_name={'verbose_name':'功能名称'},qrik_value={'verbose_name':'功能路径'})
class App(QrikBaseModel):
    """功能模块"""
    icon  = models.URLField(verbose_name="功能图标")
    
    class Meta(QrikBaseModel.Meta): 
        verbose_name = '功能模块'  
        verbose_name_plural = '功能模块'  
        
    def __unicode__(self):
        return u'%s' % (self.qrik_name)
    

@modify_fields(qrik_code={'verbose_name':'功能编码'}, qrik_name={'verbose_name':'功能名称'},qrik_value={'verbose_name':'功能路径'})
class Menu(QrikBaseModel):
    """功能菜单"""
    icon  = models.URLField(verbose_name="功能图标")
    app  = models.ForeignKey(App, verbose_name="功能模块", default=None, blank=True)
    groups = models.ManyToManyField(Group, verbose_name="用户组")
    
    class Meta(QrikBaseModel.Meta): 
        verbose_name = '功能菜单'  
        verbose_name_plural = '功能菜单'  
        
    def __unicode__(self):
        return u'%s' % (self.qrik_name)
    
@modify_fields(qrik_code={'verbose_name':'操作编码'}, qrik_name={'verbose_name':'操作名称'},qrik_value={'verbose_name':'操作路径'})
class Action(QrikBaseModel):
    """功能按钮"""
    icon  = models.URLField(verbose_name="功能图标")
    menu  = models.ForeignKey(Menu, verbose_name="功能菜单", default=None, blank=True)
    
    class Meta(QrikBaseModel.Meta): 
        verbose_name = '功能操作'  
        verbose_name_plural = '功能操作'  
        
    def __unicode__(self):
        return u'%s' % (self.qrik_name)

