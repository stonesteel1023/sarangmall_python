# -*- coding: utf-8 -*-
"""
Created on Mon May 11 00:08:23 2020

@author: stonesteel
"""
# pip install pymssql
import pymssql

conn = pymssql.connect(host='SQLOLEDB', user='Pos', password='****', database='disciples') 
cur = conn.cursor()

# cur.execute('CREATE TABLE persons(id INT, name VARCHAR(100))')
# cur.executemany("INSERT INTO persons VALUES(%d, %s)", \ [ (1, 'John Doe'), (2, 'Jane Doe') ])
# conn.commit() # you must call commit() to persist your data if you don't set autocommit to True

cur.execute('SELECT * FROM persons WHERE salesrep=%s', 'John Doe')
row = cur.fetchone()
while row: 
    print "ID=%d, Name=%s" % (row[0], row[1])
    row = cur.fetchone()

conn.close()
