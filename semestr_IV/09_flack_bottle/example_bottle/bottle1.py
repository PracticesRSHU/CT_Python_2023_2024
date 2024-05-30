from bottle import route, run

#декоратор декоратор route, щоб зв’язати URL
# з наступною функцією; зокрема, / - домашня сторінка сайту,
# що обробляється функцією home().
@route('/')
def home():
    return "<h1>It's my first home page!</h1>"

@route('/aboutme')
def home():
    return "<h1>About me!</h1>"

run(host='localhost', port=8080) #127.0.0.1:8080
