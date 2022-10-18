from re import template
from sys import exec_prefix
from urllib import request
from flask import Flask, render_template, request, redirect, session
import sqlite3 as sql

app = Flask(__name__)




@app.route('/signin')
def signin():
    return render_template('signin.html')    

@app.route('/signup')
def signup():
    return render_template('signup.html')    

@app.route('/about')
def about():
    return render_template('about.html')    

@app.route('/')
def index():
    return render_template('index.html')    


app.route('/addrec',methods = ['POST','GET'])
def addrec():
    if request.method == 'POST':
        try:
            email = request.form['email']
            password = request.form['password']
            address = request.form['address']
            city = request.form['city']
            state = request.form['state']
            zip = request.form['zip']
            
            with sql.connect("students.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students(email,password,address,city,state,zip) VALUES (?,?,?,?,?,?)",(email,password,address,city,state,zip))
                con.commit
                msg = "Record Added"
        except:
            con.rollback()
            msg = "Error in insert operation"
        finally:
            return render_template("list.html",msg=msg)
            con.close()    

@app.route('/list')
def list():
    con = sql.connect("students.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from students")

    students = cur.fetchall()
    return render_template("list.html", students = students)
if __name__ == '__main__':
    app.run(debug = True)    