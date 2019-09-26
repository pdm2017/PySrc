# db06.py

import sqlite3
print("삭제할 번호를 입력하세요")
no = input('---> ')
dbcon = sqlite3.connect('test01.db')
cursor = dbcon.cursor()
###########################################
sql = '''delete from T1 where no = ? '''
cursor.execute(sql,(int(no),))
dbcon.commit()
###########################################
cursor.close()
dbcon.close()
print("실행 완료")