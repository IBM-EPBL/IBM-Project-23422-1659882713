from turtle import st
import ibm_db

from re import template
from flask import Flask, redirect, render_template, request, session, url_for, flash
from markupsafe import escape

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=hmy36820;PWD=UFDsIyZBi3LvV6u9",'','')

app = Flask(__name__,static_url_path='/static')


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

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
  if request.method == 'POST':

    name = request.form['name']
    dob = request.form['dob']
    email = request.form['email']
    mobile = request.form['mobile']
    password = request.form['password']
    repass = request.form['repass']

    sql = "SELECT * FROM users WHERE email =?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,email)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)

    if account:
      # flash("Your email is already registered.......")
      return render_template('index.html',msg="your already registered....")
    else:
      insert_sql = "INSERT INTO users VALUES (?,?,?,?,?,?)"
      prep_stmt = ibm_db.prepare(conn, insert_sql)
      ibm_db.bind_param(prep_stmt, 1, name)
      ibm_db.bind_param(prep_stmt, 2, dob)
      ibm_db.bind_param(prep_stmt, 3, email)
      ibm_db.bind_param(prep_stmt, 4, mobile)
      ibm_db.bind_param(prep_stmt, 5, password)
      ibm_db.bind_param(prep_stmt, 6, repass)
      ibm_db.execute(prep_stmt)
    
    # flash("Your account created successfully")
    return render_template('index.html', msg="Student Data saved successfuly..")
