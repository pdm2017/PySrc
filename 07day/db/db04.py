# db04.py
import sqlite3
학생들 = {6:'Lee',7:'Kim',8:'Seo'}
dbcon = sqlite3.connect('test01.db')
cursor = dbcon.cursor()
###########################################
sql = '''insert into T1 values (?,?)'''
for i,j in 학생들.items():
    cursor.execute(sql,(i,j))
dbcon.commit()
###########################################
#for i in 학생들:
#    sql = '''insert into T1 values ({},{})'''.format(i,학생들[i])
#    cursor.execute(sql)
#dbcon.commit()
###########################################
cursor.close()
dbcon.close()
