# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendEmail(msgTo, content, type):
    (attachment,html) = content
    msg = MIMEMultipart()
    msg['Subject'] = type
    msg['From'] = 'wangdong@kmopt.com'
    msg['To'] = msgTo
    html_att = MIMEText(html, 'html', 'utf-8')
    att = MIMEText(attachment, 'plain', 'utf-8')
    msg.attach(html_att)
    msg.attach(att)
    try:
        smtp = smtplib.SMTP()
        smtp.connect('smtp.263.net', 25)
        smtp.login(msg['From'], 'wdong@0522?')
        smtp.sendmail(msg['From'], msg['To'].split(','), msg.as_string())
    except Exception,e:
        print e
            
            
            
if __name__ == '__main__':    
    ToUser='wangdong@kmopt.com'
    filestr = 'email_263.py'          
    html =  file(filestr).read()    
    sendEmail(ToUser, (filestr, html), u'测试主题')
    print "test"
