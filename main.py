
from flask import Flask, render_template, request, redirect, session, url_for
from flask_mysqldb import MySQL
import MySQLdb


app = Flask(__name__)
app.secret_key="123456"

app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] =""
app.config["MYSQL_DB"] = "user"

db = MySQL(app)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        if 'name' in request.form and "college" in request.form :
            name = request.form['name']
            college = request.form['college']
            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("SELECT * FROM tired WHERE name = %s AND College = %s",(name,college))
            info = cursor.fetchone()

            if info is not None:
               if info['name'] ==name and info["College"]==college:
                session['loginsuccess'] = True
                return redirect (url_for('profile'))
            else:
                return redirect(url_for('index'))

    return render_template("login.html")

@app.route('/new',methods=['GET','POST'])
def new_user():
    if request.method == "POST":
       if 'name' in request.form and 'college' in request.form:
          Name = request.form['name']
          College = request.form['college']
          cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
          cursor.execute("INSERT INTO tired(name,College) VALUES(%s,%s)",(Name,College))
          db.connection.commit()
          return redirect(url_for('index'))

    return render_template("register.html")


@app.route('/new/profile')
def profile():
   if  session['loginsuccess'] == True:
       return render_template('profile.html')


if __name__ == '__main__':
   app.run(debug=True)
