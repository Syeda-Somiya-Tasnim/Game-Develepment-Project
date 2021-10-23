import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="login",
)
if mydb.is_connected():
    print("Succe")