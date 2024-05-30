from bottle import route, run, static_file, request, error, get,post, Bottle
# import requests
#створіть index.html, вміст якого буде відображатися в браузері
# на URL-запит  / - домашня сторінка сайту,

app=Bottle()
@app.route('/')
def home():
    return static_file('static_files/index.html', root='.')

@app.route('/learn/<prog>')
def learn(prog):
    return "Say, let's learn the programming language: {0:s}!".format(prog)


@app.route('/image')
def home():
    return static_file('static_files/forestimage.jpeg', root='.')


@app.get('/login') # or @app.route('/login', method='GET')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" /><br>
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@app.post('/login') # or @app.route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    # if check_login(username, password):
    #     return "<p>You input correct login and password.</p>"
    # else:
    #     return "<p>Login and password not correct.</p>"
    return f"<p>You input correct login {username} and password {password} </p>"

@app.error(404)
def error404(error):
    return 'Oh, sorry this page is not found (((! Перейдіть за посиланням <a href="http://localhost:8080/">http://localhost:8080/</a>'

app.run(host='localhost', port=8080,reloader=True)

# У виклик функції run() можна додати ще такі аргументи:
# debug = True - створює сторінку налагодження, у разі отримання помилки HTTP
# reloader = True - оновлює сторінку у браузері, якщо код програми змінився
