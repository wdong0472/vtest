# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

import urllib,urllib2
import json
import sys
# Create your views here.

#!/usr/bin/python
# coding: utf-8

CORPID = 'ww2b6f426ae3b0b851'
CORPSECRET = 'JIHQgotzMGso5u-8Z8UZZ0MTkfJp8kwcszTONawKbSk'
USERLIST = [{'wdong':'王东'},{'turong':'土荣'}]

def gettoken(corpid,corpsecret):
    gettoken_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + corpid + '&corpsecret=' + corpsecret
    try:
        token_file = urllib2.urlopen(gettoken_url)
    except urllib2.HTTPError as e:
        print e.code
        print e.read().decode("utf8")
        sys.exit()
    token_data = token_file.read().decode('utf-8')
    token_json = json.loads(token_data)
    token_json.keys()
    token = token_json['access_token']
    return token

def senddata(access_token,user,content):
    send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + access_token
    send_values = {
        "touser":user,    #企业号中的用户帐号，在zabbix用户Media中配置，如果配置不正常，将按部门发送。
        "toparty":"1",    #企业号中的部门id
        "msgtype":"text",  #企业号中的应用id，消息类型。
        "agentid":"1000003",
        "text":{
            "content":content
            },
        "safe":"0"
    }
    send_data = json.dumps(send_values, ensure_ascii=False)
    send_request = urllib2.Request(send_url, send_data)
    response = json.loads(urllib2.urlopen(send_request).read())
    print str(response)

if __name__ == '__main__':
    user = str(sys.argv[1])   #zabbix传过来的第一个参数
    content = str(sys.argv[2])  #zabbix传过来的第三个参数
    corpid = CORPID   #CorpID是企业号的标识
    corpsecret = CORPSECRET  #corpsecretSecret是管理组凭证密钥
    
    accesstoken = gettoken(corpid,corpsecret)
    senddata(accesstoken,user,content)
