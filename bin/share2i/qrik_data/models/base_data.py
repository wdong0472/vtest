# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from qrik_libs.QrikBaseModel import QrikBaseModel
                
# Create your models here.
class Category(QrikBaseModel):
    # parent = models.ForeignKey('self', blank=True, default=None,verbose_name='上级类别')
    class Meta(QrikBaseModel.Meta): 
        verbose_name = '数据类别'  
        verbose_name_plural = '数据类别'  
        
    def __unicode__(self):
        return u'%s' % (self.qrik_name)
    
class CodeData(QrikBaseModel):
    category    = models.ForeignKey(Category, verbose_name="类别")
    
    class Meta(QrikBaseModel.Meta): 
        verbose_name = '数据字典'
        verbose_name_plural = '数据字典'
        
    def __unicode__(self):
        return u'%s-%s' % (self.category.qrik_name, self.qrik_name)
    
class CodeMan(QrikBaseModel):
    
    class Meta(QrikBaseModel.Meta): 
        verbose_name = 'SQL配置'
        verbose_name_plural = 'SQL配置'
        
    def __unicode__(self):
        return u'%s' % (self.qrik_name)
