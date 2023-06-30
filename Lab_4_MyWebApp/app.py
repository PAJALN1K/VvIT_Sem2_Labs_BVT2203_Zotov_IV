import requests
from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)


conn = psycopg2.connect(database="service_db",
                        user="postgres",
                        password="password1",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()


@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')


@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username and password == '':
        return render_template('login.html', error_msg='Error: the login and the password are missing.')
    elif username == '':
        return render_template('login.html', error_msg='Error: the login is missing.')
    elif password == '':
        return render_template('login.html', error_msg='Error: the password is missing.')

    cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
    records = list(cursor.fetchall())
    if len(records) == 0:
        return render_template('login.html', error_msg='Error: the login or the password is incorrect.')

    return render_template('account.html', full_name=records[0][1], username=records[0][2], password=records[0][3])
