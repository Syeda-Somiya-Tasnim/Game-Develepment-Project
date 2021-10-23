
import mysql.connector
import cgi

form = cgi.FieldStorage()

first_name=form.getvalue("first_name")   
last_name = form.getvalue("last_name")  
email	= form.getvalue("email")
new_pass=form.getvalue("new_pass")
con_pass=form.getvalue("con_pass")



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="login"
)

mycursor = mydb.cursor()

sql = "INSERT INTO  entry (first_name,last_name,email,new_pass,con_pass) VALUES (%s, %s, %s,%s,%s)"
val = (first_name,last_name	email	new_pass	con_pass)
mycursor.execute(sql, val)

mydb.commit()
mydb.close()
print(mycursor.rowcount, "record inserted.")