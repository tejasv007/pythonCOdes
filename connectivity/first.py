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
# ---- 
print("----my file is working------😊😊")
