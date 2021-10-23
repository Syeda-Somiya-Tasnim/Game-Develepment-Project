#!C:\Python39
from flask import Flask 
from flaskext.mysql import MySQL 
mysql = MySQL() 
app=Flask(__name__) 
app.config['MYSQL_DATABASE_USER'] ="username" 
app.config['MYSQL_DATABASE_PASSWORD'] = "password 
app.config['MYSQL_DATABASE_DB'] ="database name" 
app.config['MYSQL_DATABASE_HOST'] = "host_name" 
mysql.init_app(app) 
con=mysql.connect() 
cursor=con.cursor() 
@app.route('/register',methods=['POST']) 
def register(): 
	name=request.form['name'] 
	email=request.form['email'] 
    pas=request.form['pass'] 
    cursor.execute("insert into table_name values (%s,%s,%s)",		(name,email,pass)) 
	con.commit() 
    return "successfully registered" 
