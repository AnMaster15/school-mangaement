import os
import pandas as pd
try: 
  import mysql.connector as sqltor
except:
  os.system("pip install mysql-connector-python")
  import mysql.connector as sqltor


def sql_connect():
  mycon = sqltor.connect(
    host="sql6.freemysqlhosting.net",
    user="sql6467264",
    password="pfkWStZ1NA",
    port=3306,
    database="sql6467264"
  )
  return mycon


mycon=sql_connect()

if mycon.is_connected():
  print("Successfully Connected to MySql database\n")
else:
  print("MySql Connection Failed")


#df=pd.read_sql("SHOW DATABASES;", mycon)
#print(df)
mycursor = mycon.cursor()

cmdkk="insert into STUDENTS values (1000, 'Aman Singh', 1,'A', 2015-11-11, 'Amandeep Singh', 'Amandeep Kaur'),(1001, 'Ayush Sinha',1, 'A', 2015-4-1,'Ayushdeep sinha', 'Ayushdeep Kaur');"


cmd="SELECT * FROM STUDENTS;"

cmd='''USE sql6467264; insert into STUDENTS values (2000, 'Jona Choy', 12,'A', '2004-11-11', 'Jona dad', 'Jona mom');'''

#mycursor.execute(cmd,multi=True)

#cmd="DESC STUDENTS"
'''try:
  
  myresult = mycursor.fetchall()
  for x in myresult:
    print(x)

except Exception as e:
  print("hi")
  print(e)'''

sql = "INSERT INTO STUDENTS (name, AdmNo) VALUES ('Tom',2003);"
mycursor.execute(sql)
mycon.commit()


df=pd.read_sql("select * from STUDENTS", mycon)
print(df)