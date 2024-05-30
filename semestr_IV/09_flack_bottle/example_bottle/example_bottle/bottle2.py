from bottle import route, run, static_file

#створіть index.html, вміст якого буде відображатися в браузері
# на URL-запит  / - домашня сторінка сайту,
@route('/')
def home():
    return static_file('index.html', root='static_files')

run(host='localhost', port=8080)
