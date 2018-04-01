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

if __name__ == '__main__':
    #这里使用SMTP_SSL就是默认使用465端口
    smtp = SMTP_SSL(mail_info["hostname"])
    smtp.set_debuglevel(1)
    
    smtp.ehlo(mail_info["hostname"])
    smtp.login(mail_info["username"], mail_info["password"])

    msg = MIMEText(mail_info["mail_text"], "plain", mail_info["mail_encoding"])
    msg["Subject"] = Header(mail_info["mail_subject"], mail_info["mail_encoding"])
    msg["from"] = mail_info["from"]
    msg["to"] = mail_info["to"]
    
    smtp.sendmail(mail_info["from"], mail_info["to"], msg.as_string())
    print "ok"
    smtp.quit()
    
    # #这里使用SMTP_SSL就是默认使用465端口
    # smtp = SMTP_SSL(mail_info["hostname"])
    # smtp.set_debuglevel(1)
    # smtp.ehlo(mail_info["hostname"])
    # smtp.login(mail_info["username"], mail_info["password"])
    
    # msg = MIMEMultipart() 
    # msg = MIMEText(mail_info["mail_text"], "plain", mail_info["mail_encoding"])
    # msg["Subject"] = Header(mail_info["mail_subject"], mail_info["mail_encoding"])
    # msg["from"] = mail_info["from"]
    # msg["to"] = mail_info["to"]
    # msg['Date'] = formatdate(localtime=True) 
    # msg.attach(MIMEText(text)) 
    
    
    # file = request.FILES['to_file']
    
    # part = MIMEBase('application', 'octet-stream') #'octet-stream': binary data 
    # part.set_payload(file.file.getvalue()) 
    # encoders.encode_base64(part) 
    # part.add_header('Content-Disposition', 'attachment; filename="%s"' % file.name) 
    # msg.attach(part) 
    
    # smtp.sendmail(mail_info["from"], mail_info["to"], msg.as_string())
    # print "ok"
    # smtp.quit()
