```
> !/usr/bin/python
>  -*- coding: UTF-8 -*-
import time
from workload import sqlmodule


db_name = '/app/sqlite/workload.db'


# 初始化数据库表
table_name = 'blade'
table = ' (id INTEGER PRIMARY KEY AUTOINCREMENT, uuid BLOB,model BLOB,sn BLOB, insert_time text,rack BLOB,slot int)'
# sqlmodule.create_db(db_name,table_name,table)


# 插入数据
key = 'uuid, model ,insert_time'
value = {'uuid':sqlmodule.createuuid4(),'model':'RH2288V2', 'insert_time': time.strftime('%Y-%b-%d ', time.localtime())}

execsql = '''INSERT INTO {table1}
({key})
values 
(:uuid, :model ,:insert_time)
'''.format(table1=table_name,key= key)

sqlmodule.save_to_db(db_name,execsql,value)
```

```
# coding=utf-8
import os
import sqlite3
from uuid import uuid4

def createuuid4():
    returnuuid4 = str(uuid4()).replace('-', '')
    return  returnuuid4

def getpathdir(PATH):
    return os.listdir(PATH)

# 创建数据库 及 表,不存在则创建
def create_db(db_name,table_name,table):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    sql = 'DROP TABLE IF EXISTS ' + table_name
    c.execute(sql)
    sql2 = 'CREATE TABLE ' + table_name + table
    c.execute(sql2)
    conn.close()

def save_to_db(db_name,execsql,value):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(execsql,value)
    conn.commit()
    conn.close()

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
# 返回dict格式的结果
def select_db(db_name,execsql):
    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory
    c = conn.cursor()
    results = c.execute(execsql)
    results1 =results.fetchall()
    conn.close()
    return results1

def update_table(db_name,updatesql):
    print (updatesql)
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute(updatesql)
    conn.commit()
    conn.close()

```
