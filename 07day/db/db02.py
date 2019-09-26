# db02.py
import sqlite3
dbcon = sqlite3.connect('test01.db')
cursor = dbcon.cursor()
###########################################
sql = '''insert into T1 values (50,'Sophia') '''
cursor.execute(sql)
#cursor.execute('commit')
dbcon.commit()
###########################################
cursor.close()
dbcon.close()