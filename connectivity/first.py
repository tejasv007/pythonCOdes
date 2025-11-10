# # firstly for connectivity, import library
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Handge@2609#",database="bittu")
mycursor=mydb.cursor()
# ----for showing all data bases1️⃣
# mycursor.execute("show databases;")
# for i in mycursor:
#     print(i[0])
# ----for creating a database2️⃣
# try:
#     mycursor.execute("create database BITTU;")
# except:
#     print("database exists")
# ----for creatng a table3️⃣
# table1='''create table NEW (id int auto_increment primary key,name varchar(100),age int)'''
# mycursor.execute(table1)
# ---for showing table4️⃣
# mycursor.execute("show tables;")
# print("tables in my database: ")
# for i in mycursor:
#     print(i[0])
# ----for insertion of a record5️⃣
# insert1="insert into new(name, age) values(%s,%s)"
# insertD=("anu",20)
# mycursor.execute(insert1,insertD)
# mydb.commit()
# ---- select record6️⃣
# cmdSel="select * from bittu.new;"
# mycursor.execute(cmdSel)
# myres=mycursor.fetchall()
# print(myres)
# ---- can insert many record7️⃣
# insert1="insert into new(name, age) values(%s,%s)"
# dbList=[("rani",30),("gita",23),("hira",21)]
# mycursor.executemany(insert1,dbList)
# mydb.commit()
# ---- update record8️⃣
# upRec="update bittu.new set age=%s where name= %s"
# setVal=(24,"rani")
# mycursor.execute(upRec,setVal)
# mydb.commit()
# print(mycursor.re)
# ----delete record9️⃣
# delRec="delete from bittu.new where name=%s"
# dbValue=("gita",)
# mycursor.execute(delRec,dbValue)
# mydb.commit()
# --- delete a table🔟
# cmd="drop table new"
# mycursor.execute(cmd)
# mydb.commit()
# ----delete whole data of a table but table is intact1️⃣1️⃣
# cmd="truncate table bittu.new"
# mycursor.execute(cmd)
# mydb.commit()
print("----my file is working------😊😊")
