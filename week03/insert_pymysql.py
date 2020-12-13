#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:My
@file:insert_pymysql.py
@time:2020/12/13
"""

# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:My
@file:mode3_pymysql_conn.py
@time:2020/12/13
"""

import pymysql

db = pymysql.connect("localhost", "testuser", "testpass", "testdb")
try:
    with db.cursor() as cursor:
        sql = ''' insert into student values (1,'Scott', 34, '1986-05-01','1', '本科', null,null),
        (2,'Mary', 24, '1996-06-01', 0, '硕士', null,null),
        (3,'Jack', 35, '1985-09-01', 0, '博士', null,null)'''
        cursor.execute(sql)
    db.commit()
except Exception as e:
    print(f"error {e}")
finally:
    db.close()

print('have commit')
