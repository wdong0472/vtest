# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime


def get_weather(s):
    r = requests.get('http://www.weather.com.cn/data/sk/101290101.html')
    r.encoding = 'utf-8'
    #print r.json()['weatherinfo']['city'], r.json()['weatherinfo']['WD'], r.json()['weatherinfo']['temp']
    print r.json()

    client = MongoClient('share2i.com',27017)    
    db = client.admin
    db.authenticate("root", "root")
    weathers = db.weathers
    weathers.save(r.json()) # add a record


def aps_test(x):
    print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.daemonic = False  
    #scheduler.add_job(func=aps_test, args=('定时任务',), trigger='cron', second='*/5')
    #scheduler.add_job(func=aps_test, args=('一次性任务',), next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=12))
    scheduler.add_job(func=get_weather, args=('循环任务',), trigger='interval', seconds=60)
    scheduler.add_job(func=get_weather, args=('循环任务',), trigger='interval', hours=24)

    scheduler.start()
