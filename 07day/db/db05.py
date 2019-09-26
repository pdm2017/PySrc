# db05.py
import sqlite3
print("이름을 수정할 번호는? 예) 5 Hong")
no, name = input('----> ').split()
dbcon = sqlite3.connect('test01.db')
cursor = dbcon.cursor()
###########################################
sql ='''update T1 set name = ? where no = ? '''
cursor.execute(sql, (name, no))
dbcon.commit()
###########################################
cursor.close()
dbcon.close()
print("실행 완료")
