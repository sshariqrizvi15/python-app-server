from flask import Flask
from flaskext.mysql import MySQL
import json

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'shariq'
app.config['MYSQL_DATABASE_PASSWORD'] = 'shariq12'
app.config['MYSQL_DATABASE_DB'] = 'dbname'
app.config['MYSQL_DATABASE_HOST'] = 'shariqdatabase1.ccvyw5hnor6i.us-east-2.rds.amazonaws.com'
mysql = MySQL()
mysql.init_app(app)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/app/checkRequest')
def checkRequest():
   cur = mysql.connect().cursor()
   cur.execute('''select * from Person limit 1''')
   row_headers=[x[0] for x in cur.description] #this will extract row headers
   rv = cur.fetchall()
   json_data=[]
   for result in rv:
        json_data.append(dict(zip(row_headers,result)))
   return json.dumps(json_data[0])

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = False)