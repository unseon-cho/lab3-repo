
from flask import Flask
from flask_mysqldb import MySQL
mysql = MySQL()
app = Flask(__name__)
# My SQL Instance configurations 
# Change the HOST IP and Password to match your instance configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '9X9_6c6N'
app.config['MYSQL_DB'] = 'studentbook'
app.config['MYSQL_HOST'] = '35.195.77.155'
mysql.init_app(app)

# The first route to access the webservice from http://external-ip:5000/ 
#@pp.route("/add") this will create a new endpoints that can be accessed using http://external-ip:5000/add
@app.route("/")
def hello(): # Name of the method
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''INSERT INTO students (studentName, email) values ("third", "third@mydit.ie")''');
    cur.execute('''UPDATE students set studentName="second" where studentName="second student"''');
    cur.execute('''DELETE from students where studentName="first student"''');
    cur.execute('''SELECT * FROM students''') # execute an SQL statment
    rv = cur.fetchall() #Retreive all rows returend by the SQL statment
    return '''<html><body><h1>'''+str(rv)+'''</h1></body></html>'''      #Return the data in a string format
if __name__ == "__main__":
        app.run(host='0.0.0.0', port='5000') #Run the flask app at port 5000

