# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.apps import AppConfig

default_app_config = 'tpm.QrikUiConfig'
VERBOSE_APP_NAME = u"UI组件"


def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]
    
class QrikUiConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_APP_NAME
