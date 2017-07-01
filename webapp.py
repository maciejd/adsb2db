#!flask/bin/python
from flask import Flask,render_template
import sqlite3 as sql
import datetime

app = Flask(__name__)

@app.route('/list')
def list():
   con = sql.connect("app.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select hex,flight,timestamp as date from aircrafts where flight != '' order by timestamp desc")
   
   rows = cur.fetchall(); 
   return render_template("list.html",rows = rows)

@app.template_filter('datetime')
def datetimeformat(value, format='%H:%M / %d-%m-%Y'):
    return datetime.datetime.fromtimestamp(value).strftime(format)

if __name__ == '__main__':
    app.run(debug=True)
