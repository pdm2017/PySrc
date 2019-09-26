# db03.py
import sqlite3
dbcon = sqlite3.connect('test01.db')
cursor = dbcon.cursor()
###########################################
sql = ''' update T1 set no = no/10 '''
cursor.execute(sql)
dbcon.commit()
###########################################
cursor.close()
dbcon.close()