#!C:\Python39


import mysql.connector
import cgi

form = cgi.FieldStorage()

n=form.getvalue("name")   
e = form.getvalue("emailid")  
p = form.getvalue("password")



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="login"
)

mycursor = mydb.cursor()

sql = "INSERT INTO reg_tb (name, email, pass) VALUES (%s, %s, %s)"
val = (n, e, p)
mycursor.execute(sql, val)

mydb.commit()
mydb.close()
print(mycursor.rowcount, "record inserted.")