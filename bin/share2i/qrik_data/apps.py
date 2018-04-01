# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.apps import AppConfig

default_app_config = 'tpm.QrikDataConfig'
VERBOSE_APP_NAME = u"基础信息"


def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]
    
class QrikDataConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_APP_NAME
