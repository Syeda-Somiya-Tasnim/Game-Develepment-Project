#!C:\Python39
import cgi


import mysql.connector
import cgi

form = cgi.FieldStorage()

n=form.getvalue("name")   #from html page
e = form.getvalue("email")  #from html page
p = form.getvalue("pass")   #from html page



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="SDM"
)

mycursor = mydb.cursor()

sql = "INSERT INTO reg_tb (name, email, pass) VALUES (%s, %s, %s)"
val = (n, e, p)
mycursor.execute(sql, val)

mydb.commit()
mydb.close()
print(mycursor.rowcount, "record inserted.")