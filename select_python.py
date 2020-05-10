# -*- coding: utf-8 -*-
"""
Created on Mon May 11 00:08:23 2020

@author: stonesteel
"""
# pip install pymssql
# pymssql 패키지 import
import pymssql
# MSSQL 접속
# conn = pymssql.connect(host=r"(local)", database='MyDB', charset='utf8')
conn = pymssql.connect(host='SQLOLEDB', user='Pos', password='****', database='disciples')

# Connection 으로부터 Cursor 생성
cur = conn.cursor()

# cur.execute('CREATE TABLE persons(id INT, name VARCHAR(100))')
# cur.executemany("INSERT INTO persons VALUES(%d, %s)", \ [ (1, 'John Doe'), (2, 'Jane Doe') ])
# conn.commit() # you must call commit() to persist your data if you don't set autocommit to True

# SQL문 실행
cur.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')

# 데이타 하나씩 Fetch하여 출력
row = cur.fetchone()
while row: 
    print "ID=%d, Name=%s" % (row[0], row[1])
    row = cur.fetchone()

# 연결 끊기
conn.close()
