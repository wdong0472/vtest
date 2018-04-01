# -*- coding: utf-8 -*-
"""share2i URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static

from . import settings
from . import views
from qrik_ui.views import index  

urlpatterns = [
    #url(r'^WW_verify_sxePFKn2shUsFB6V\.txt/$', TemplateView.as_view(template_name='WW_verify_sxePFKn2shUsFB6V.txt',  
    #                                             content_type='text/txt')),
    url(r'^$', index),
    url(r'^index/$', index),
    url(r'^saveurls/$', views.save_urls),
    url(r'^syncbookmarks/$', views.sync_bookmarks),  
    url(r'^sendmail/$', views.send_mymail2),  
    url(r'^saveimg/$', views.save_image),  
    url(r'^savepage/$', views.save_page),  
    url(r'^admin/', admin.site.urls),
    url(r'^qrik_ui/', include('qrik_ui.urls',namespace="qrik_ui")),
    url(r'^qrik_test/', include('qrik_test.urls',namespace="qrik_test")),
    url(r'^qrik_demo/', include('qrik_demo.urls',namespace="qrik_demo")),
    url(r'^qrik_widgets/', include('qrik_widgets.urls',namespace="qrik_widgets")),  
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) 
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
