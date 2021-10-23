import os

import mysql.connector
from flask import Flask, redirect, render_template, request, session

app=Flask(__name__)
app.secret_key=os.urandom(24)

conn=mysql.connector.connect(host="localhost",user="root",password="",database="users")
cursor=conn.cursor()

@app.route('/')
def login():
    return render_template('loginluv.html')

@app.route('/register')
def about():
    return render_template('register.html')

@app.route('/choose')
def home():
    if 'user_id' in session:
       return render_template('choose.html')
    else:
       return redirect('/') 
@app.route('/snake')
def snake():
    return render_template('Snake.html')

@app.route('/tetris')
def tetris():
    return render_template('tetris.html')

@app.route('/tictactoe')
def tictactoe():
    return render_template('tictactoe.html')

@app.route('/sp')
def sp():
    return render_template('snake.py')

@app.route('/tep')
def tep():
    return render_template('tetris.py')

@app.route('/tip')
def tip():
    return render_template('tictactoe.py')

@app.route('/sabout')
def sabout():
    return render_template('instsnake.html')

@app.route('/teabout')
def teabout():
    return render_template('instetris.html')
    
@app.route('/tiabout')
def tiabout():
    return render_template('instic.html')

@app.route('/sscore')
def sscore():
    return render_template('hs-snake.html')

@app.route('/tescore')
def tescore():
    return render_template('hs-tetris.html')

@app.route('/tiscore')
def tiscore():
    return render_template('hs-tictactoe.html')

@app.route('/back')
def back():
    if 'user_id' in session:
           return render_template('choose.html')
    else:
       return redirect('snake.html') 

@app.route('/login_validation', methods=['POST'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')

    cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email,password))
    users=cursor.fetchall()
    if len(users)>0:
        session['user_id']=users[0][0]
        return redirect('/choose')
    else:
        return redirect('/')

@app.route('/add_user', methods=['POST'])
def add_user():
    name=request.form.get('uname')
    email=request.form.get('uemail')
    password=request.form.get('upassword')

    cursor.execute("""INSERT INTO `users` (`user_id`,`name`,`email`,`password`) VALUES 
    (NULL,'{}','{}','{}')""".format(name,email,password))
    conn.commit()

    cursor.execute("""SELECT * FROM `users` WHERE `email` LIKE '{}' """.format(email))
    myusers=cursor.fetchall()
    session['user_id']=myusers[0][0]
    return redirect('/choose')
@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/')


    
if __name__=="__main__":
    app.run(debug=True)


