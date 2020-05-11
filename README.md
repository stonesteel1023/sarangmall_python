# sarangmall_python

## python 3.7.7 다운로드
https://www.python.org/ftp/python/3.7.7/python-3.7.7-amd64.exe

## 에러발생시 추가 다운로드
https://download.microsoft.com/download/5/F/7/5F7ACAEB-8363-451F-9425-68A90F98B238/visualcppbuildtools_full.exe

## pymssql 직접 다운로드 & 사용법
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pymssql
> https://code.google.com/archive/p/pymssql/


## 순서

1. pymssql 모듈을 import 한다

2. pymssql.connect() 메소드를 사용하여 MSSQL에 Connect 한다. 호스트명, 로그인, 암호, 접속할 DB 등을 파라미터로 지정할 수 있다.

3. DB 접속이 성공하면, Connection 객체로부터 cursor() 메서드를 호출하여 Cursor 객체를 가져온다. DB 커서는 Fetch 동작을 관리하는데 사용된다.

4. Cursor 객체의 execute() 메서드를 사용하여 SQL 문장을 DB 서버에 보낸다.

5. SQL 쿼리의 경우 Cursor 객체의 fetchall(), fetchone(), fetchmany() 등의 메서드를 사용하여 데이타를 서버로부터 가져온 후, Fetch 된 데이타를 사용한다.

6. 삽입, 갱신, 삭제 등의 DML(Data Manipulation Language) 문장을 실행하는 경우, INSERT/UPDATE/DELETE 후 Connection 객체의 commit() 메서드를 사용하여 데이타를 확정 갱신한다.

7. Connection 객체의 close() 메서드를 사용하여 DB 연결을 닫는다.
