# -*- coding: utf-8 -*-
import pymssql
server  =       '172.16.134.129'
user    =       'sa'
password =      '1qaz@WSX?'

conn    = pymssql.connect(server,user,password,"t")
cursor  = conn.cursor()
sql     = 'select count(*) from t_1'
cursor.execute(sql)
row     = cursor.fetchone()
print (row[0])
conn.close()
