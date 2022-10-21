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

print("before route")

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         name = request.form['name']
         addr = request.form['address']
         city = request.form['city']
         pin = request.form['pin']
         
         with sql.connect("student_database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(name,addr,city,pin) )
            con.commit()
            msg = "Record successfully added!"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("list.html",msg = msg)
         con.close()



@app.route('/list')
def list():
   con = sql.connect("student_database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   students = cur.fetchall();
   return render_template("list.html", students = students)

if __name__ == '__main__':
   app.run(debug = True)