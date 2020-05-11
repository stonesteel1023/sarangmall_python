# -*- coding: utf-8 -*-
"""
Created on Mon May 11 00:08:23 2020
@author: stonesteel
"""
# pip install Cython
# pip install pymssql
# pymssql 패키지 import
import pymssql
# MSSQL 접속
# conn = pymssql.connect(host=r"(local)", database='MyDB', charset='utf8')
conn = pymssql.connect(host='****', user='Pos', password='****', database='disciples')

# Connection 으로부터 Cursor 생성
cur = conn.cursor()

# cur.execute('CREATE TABLE persons(id INT, name VARCHAR(100))')
# cur.executemany("INSERT INTO persons VALUES(%d, %s)", \ [ (1, 'John Doe'), (2, 'Jane Doe') ])
# conn.commit() # you must call commit() to persist your data if you don't set autocommit to True

# SQL문 실행
cur.execute('SELECT SUBSTRING(orderno, 16, 5), ' \
    + 'd_id, process_info, process_date from [dbo].[sme_T_order] ' \
    + 'where process_date > %s and d_id is not null and process_info = "DF" ' \
    + 'and len(orderno) = 20 ' \
    + 'order by ottid desc', '2020-05-11')

# 데이타 하나씩 Fetch하여 출력
row = cur.fetchone()
while row: 
    print ('ID=%d, Name=%s' % row[0], row[1])
    row = cur.fetchone()

# 연결 끊기
conn.close()


### 현재 발생하고 있는 에러
> D:\python_workspace\sarangmall_python\select_python.py:10: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated since Python 3.3, and in 3.9 it will stop working
  import pymssql
Traceback (most recent call last):
  File "src\pymssql.pyx", line 448, in pymssql.Cursor.execute
  File "src\_mssql.pyx", line 1064, in _mssql.MSSQLConnection.execute_query
  File "src\_mssql.pyx", line 1095, in _mssql.MSSQLConnection.execute_query
  File "src\_mssql.pyx", line 1228, in _mssql.MSSQLConnection.format_and_run_query
  File "src\_mssql.pyx", line 1639, in _mssql.check_cancel_and_raise
  File "src\_mssql.pyx", line 1683, in _mssql.maybe_raise_MSSQLDatabaseException
_mssql.MSSQLDatabaseException: (207, b"Invalid column name '2020-05-11'.DB-Lib error message 20018, severity 16:\nGeneral SQL Server error: Check messages from the SQL Server\nDB-Lib error message 20018, severity 16:\nGeneral SQL Server error: Check messages from the SQL Server\n")

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\python_workspace\sarangmall_python\select_python.py", line 23, in <module>
    cur.execute('SELECT SUBSTRING(orderno, 16, 5), ' \
  File "src\pymssql.pyx", line 465, in pymssql.Cursor.execute
pymssql.ProgrammingError: (207, b"Invalid column name '2020-05-11'.DB-Lib error message 20018, severity 16:\nGeneral SQL Server error: Check messages from the SQL Server\nDB-Lib error message 20018, severity 16:\nGeneral SQL Server error: Check messages from the SQL Server\n")
