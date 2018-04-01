# -*- coding: utf-8 -*-
"""
    qrik_tools.models.config
    ~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Module that implements the Qrik Team Dev Tools Model Def.
    
    :copyright: Copyright 2006-2017 by the Qrik team, see AUTHORS.
    :license: WTFPL, see LICENSE for details.
    :author: wdong@2017-07-03
"""
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from qrik_libs.QrikBaseModel import QrikBaseModel

#第一个参数是真正的model参数，#第二个参数则是方便人们理解阅读
# Create your models here.
class Context(QrikBaseModel):
    CONTEXT_CATEGORY_CHOICES = (
        ('Html', 'Html模板'),
        ('Css', 'Css模板'),
        ('Js', 'Js模板'),
    )
    template = models.CharField(
        max_length=10,
        choices=CONTEXT_CATEGORY_CHOICES,
        default='Html',
        verbose_name='模板'
    )
   
    class Meta(QrikBaseModel.Meta):  
        verbose_name = '模板'  
        verbose_name_plural = '模板'
        
    def __unicode__(self):
        return u'%s' % (self.qrik_name)    
    
    
class ContextVar(QrikBaseModel):
    context = models.ForeignKey(Context, verbose_name="模板")
    
    class Meta(QrikBaseModel.Meta): 
        verbose_name = '变量'  
        verbose_name_plural = '变量'
        
    def __unicode__(self):
        return u'%s-%s' % (self.context.qrik_name, self.qrik_name)
