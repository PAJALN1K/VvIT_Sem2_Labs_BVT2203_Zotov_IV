from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)


conn = psycopg2.connect(database="service_db",
                        user="postgres",
                        password="pantera377",
                        host="localhost",
                        port="3228")

cursor = conn.cursor()


@app.route('/login/', methods=['POST', 'GET'])
def login():
    #   Если на начальной странице пользователь нажал на кнопку регистрации или авторизации, то будет использоваться
    # метод POST.
    if request.method == 'POST':
        #   Если пользователь воспользовался кнопкой для авторизации, то начнется выполнение следующего кода.
        if request.form.get("login"):
            #   Присваивание переменным username и password значений логина и пароля, которые пользователь ввел на сайт.
            username = request.form.get('username')
            password = request.form.get('password')
            #   Обработка исключений: если username и password пустые, то пользователь будет вновь перекинут на страницу
            # авторизации с соответствующим сообщением об ошибке.
            if username == '' and password == '':
                return render_template('login.html', error_msg='Error: the login and the password are missing.')
            elif username == '':
                return render_template('login.html', error_msg='Error: the login is missing.')
            elif password == '':
                return render_template('login.html', error_msg='Error: the password is missing.')
            #   Отображение в БД всех пользователей с соответствующими именами и паролями и присваивание переменной
            # records значения таблицы этих пользователей в виде списка.
            cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
            records = list(cursor.fetchall())
            #   Обработка исключений: если логина и пароля пользователя нет в БД, значит, он ввел некорректные данные.
            if len(records) == 0:
                return render_template('login.html', error_msg='Error: the login or the password is incorrect.')
            #   Если ошибок нет, то сайт будет отображаться в соответствии с содержанием файла account.html.
            return render_template('account.html', full_name=records[0][1], username=records[0][2],
                                   password=records[0][3])
        #   Если пользователь воспользовался кнопкой для регистрации, то его перенесет по адресу /registration/.
        elif request.form.get("registration"):
            return redirect("/registration/")
    #   По умолчанию при входе на страницу используется метод GET, и сайт отображается в соответствии с содержанием
    # файла login.html.
    return render_template('login.html')


@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        name = request.form.get('name')
        login = request.form.get('login')
        password = request.form.get('password')
        #   Обработка исключений: если пользователь ввел пустые данные, то будет выведена сообщение о соответствующей
        # ошибке.
        if name == '' or password == '' or login == '':
            return render_template('registration.html', error_msg='Error: the data are missing.')
        #   Обработка исключений: если пользователь ввел логин, который уже есть в БД, то будет выведено сообщение о
        # соответствующей ошибке.
        cursor.execute('SELECT login from service.users')
        records = list(cursor.fetchall())
        if login in list(records[i][0] for i in range(len(records))):
            return render_template('registration.html', error_msg='Error: this login has already been taken.')

        cursor.execute('INSERT INTO service.users (full_name, login, password) VALUES (%s, %s, %s);',
                       (str(name), str(login), str(password)))
        conn.commit()

        return redirect('/login/')
    return render_template('registration.html')
