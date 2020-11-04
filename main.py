from os import name

from flask import Flask, render_template, request, redirect, session, url_for
from flask_mysqldb import MySQL
import MySQLdb


app = Flask(__name__)

app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] =""
app.config["MYSQL_DB"] = "user"

db = MySQL(app)

@app.route('/', methods=['GET','POST'])
def index(roll=None):
    if request.method == 'POST':
        if 'name' in request.form and 'college' in request.form :
            Name = request.form['name']
            College = request.form['College']

            cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("SELECT * FROM tired WHERE name=%s and college=%s" , (Name, College))
            info = cursor.fetchone()
            if info['name'] == Name and info['college'] == College :

               return "login Successful"

            else:
               return "unsuccessful,Please Register"

    return render_template("login.html")



if __name__ == '__main__':
    app.run(debug=True)
