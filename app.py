import requests
from flask import Flask, render_template,request,redirect
import psycopg2

app = Flask(__name__)
conn=psycopg2.connect(database="service_db",
                      user="postgres",
                      password="12345",
                      host="localhost",
                      port="5432")
cursor=conn.cursor()


@app.route('/login/',methods=['post','get'])
def login():
    if request.method =='POST':
        if request.form.get("login"):
            
            username=request.form.get('username')
            password=request.form.get('password')
            cursor.execute("select * from service.users where login ='{}' and password = '{}'".format(str(username),str(password)))
            records=list(cursor.fetchall())
            return render_template('account.html',b_data=records[0][1:])
        elif request.form.get("registration"):
            return redirect ("/registration/")
    return render_template('login.html')                        
@app.route('/registration/',methods=['post','get'])
def registration():
    if request.method =='POST':
        name= request.form.get('name')
        login= request.form.get('login')
        password= request.form.get('password')
        cursor.execute("select * from service.users where login ='{}' ".format(str(username)))
        records=list(cursor.fetchall())
        if len (records)==0 or len(password)!=0:
            cursor.execute("insert into service.users (full_name, login, password) values ('{}','{}','{}')".format(str(name),str(login),str(password)))
            conn.commit()
            return redirect ('/login/')
        return render_template ('registration.html')
        
    return render_template ('registration.html')
