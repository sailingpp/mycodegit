
import mysql.connector
import pymysql

conn=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='sailing',
    db='world',
    charset='utf8'
)
cursor=conn.cursor()
sql="select * from city"
cursor.execute(sql)
result=cursor.fetchall()
for row in result:
    print(row)
cursor.close()
conn.close()