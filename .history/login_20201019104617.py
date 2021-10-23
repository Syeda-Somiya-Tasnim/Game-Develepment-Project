from flask import Flask, render_template, request
from passlib.hash import sha256_crypt
import mysql.connector as mariadb
app = Flask(__name__)
maraidb_connection = mariadb.connect(user='chooseAUserName', password='chooseAPassword', database='Login')
@app.route('/')
def index():
  username = "newUserName"
  password = sha256_crypt.encrypt("newPassword")
  email = "what@ever.com"

  cur = mariadb_connection.cursor()
  cur.execute('INSERT INTO Login (username, password, email) VALUES (%s, %s, %s)', (username, password, email))
  mariadb_connection.commit()
  cur.close()

  return "New user added"
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port='5000')