# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# mongodb
import pymongo
from pymongo import MongoClient
import demjson
from bson import json_util as jsonb
import time
import re

# send_mail
from django.core.mail import send_mail, EmailMultiAlternatives
from . import  settings

# upload_file
from django import forms
import mimetypes

def save_urls(request): 
    tags = 'test'
    user = 'wdong' #request.POST.get('user')
    url = request.POST.get('url')
    title = request.POST.get('title')
    category = request.POST.get('category')
    stamp = time.strftime('%Y-%m-%d %H:%I:%S',time.localtime(time.time()))

    client = MongoClient('share2i.com',27017)    
    db = client.admin
    db.authenticate("root", "root")
    myurls = db.myurls
    myurls.save({"tags":tags, "user":user, "url":url, "title":title, "category":category,"stamp":stamp}) # add a record
    
    return HttpResponse("ok")


def sync_bookmarks(request): 
    if request.method == 'POST':
        arr = request.POST.getlist('bookmarks[]')        

        data = demjson.decode(arr[0])
        
        client = MongoClient('share2i.com',27017)    
        db = client.admin
        db.authenticate("root", "root")
        
        bookmarks = db.bookmarks
        bulk = bookmarks.initialize_ordered_bulk_op()
        
        for i in data:
            bulk.insert(i)
        
        bulk.execute()
        
        #
        #bookmarks.save(data) # add a record
    return HttpResponse("ok")
        
def send_mymail(request):
    if request.method == "POST":
        to_user = request.POST.get('to_user')
        to_subject = request.POST.get('to_subject')
        to_content = request.POST.get('to_content')
        file = request.FILES['to_file']    
        
        # subject 主题 content 内容 to_addr 是一个列表，发送给哪些人
        msg = EmailMultiAlternatives(to_subject, to_content, settings.DEFAULT_FROM_EMAIL, [to_user])
        msg.content_subtype = "text/html"
        # 添加附件（可选）
        msg.attach(file.name, file.file.getvalue(), mimetypes.guess_type(file.name)[0])
        #email.attach(self.report_filename.format(report_id), attachment.data, "application/octet-stream")
        
        # 发送
        msg.send()
        
        # send_mail的参数分别是  邮件标题，邮件内容，发件箱(settings.py中设置过的那个)，收件箱列表(可以发送给多个人),失败静默(若发送失败，报错提示我们)
        #send_mail(to_subject, to_content, settings.EMAIL_HOST_USER, [to_user], fail_silently=False)
        # html =  file(filestr).read()    
        # _sendEmail(ToUser, (filestr, html), u'')
        print "send ok"
        return HttpResponse("ok")


    # -*- coding: UTF-8 -*-
    
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

# python 2.3.*: email.Utils email.Encoders
from email.utils import COMMASPACE,formatdate
from email import encoders

mail_info = {
    "from": "28358358@qq.com",
    "to": "wangdong@kmopt.com",
    "hostname": "smtp.qq.com",
    "username": "28358358@qq.com",
    "password": "wdong@0522?",
    "mail_subject": "test",
    "mail_text": "hello, this is a test email, sended by py",
    "mail_encoding": "utf-8"
}

def send_mymail2(request):
    if request.method == "POST":
        to_user = request.POST.get('to_user')
        to_subject = request.POST.get('to_subject')
        to_content = request.POST.get('to_content')
        file = request.FILES['to_file']    
    
        #这里使用SMTP_SSL就是默认使用465端口
        smtp = SMTP_SSL(mail_info["hostname"])
        smtp.set_debuglevel(1)
        smtp.ehlo(mail_info["hostname"])
        smtp.login(mail_info["username"], mail_info["password"])
        
        msg = MIMEMultipart('alternative') 
       
        msg2 = MIMEText(mail_info["mail_text"], "plain", mail_info["mail_encoding"])
        msg["Subject"] = Header(mail_info["mail_subject"], mail_info["mail_encoding"])
        msg["from"] = mail_info["from"]
        msg["to"] = mail_info["to"]
        msg['Date'] = formatdate(localtime=True) 
        
        
        msg.attach(msg2) 
        
        part = MIMEBase('application', 'octet-stream') #'octet-stream': binary data 
        part.set_payload(file.file.getvalue()) 
        encoders.encode_base64(part) 
        part.add_header('Content-Disposition', 'attachment', filename=Header(file.name, 'utf-8').encode()) 
        
        msg.attach(part) 
        
        smtp.sendmail(mail_info["from"], mail_info["to"], msg.as_string())
        smtp.quit()
        
        print "ok"
        
        return HttpResponse("ok")
    

from django import forms


class UploadFileForm(forms.Form):
    file_obj = forms.FileField()
    professionalfile = forms.FileField()
    
def save_image(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        file_obj = request.FILES.get('blob','') #获取上传文件
        with open("test123.png", 'w') as f:
            f.write(file_obj.read())
            
        return HttpResponse("ok")
        

def save_page(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        file_obj = request.FILES.get('mhtml','') #获取上传文件
        with open("test123.mhtml", 'w') as f:
            f.write(file_obj.read())
            
        return HttpResponse("ok")
    
def get_categorys(request):
    return json.dump(settings.URL_CATEGORY)
    
