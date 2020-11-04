import  mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="user")

mycursor = mydb.cursor()

mycursor.execute("select * from tired")

for i in mycursor:
    print(i)