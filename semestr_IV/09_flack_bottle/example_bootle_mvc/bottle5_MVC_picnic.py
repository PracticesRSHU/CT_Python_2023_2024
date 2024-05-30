import sqlite3
from bottle import route, run, template, view

#визначаємо маршрут, який відповідає URL-шляху  "/":
@route('/')
def home():
   return """<h1 style="color:red;"> Main page</h1>"""

#визначаємо маршрут, який відповідає URL-шляху  "/picnic":
@view('bring_to_picnic')
@route('/picnic')
def show_picnic():
   db = sqlite3.connect('picnic.db') # Команда, яка підключається до бази даних picnic.db
   # Запит до базу даних і вибірка всіх значення за допомогою наступних чотирьох рядків:
   c = db.cursor()
   c.execute("SELECT item, counts FROM picnic")
   data = c.fetchall()
   print(data)
   print(dict(rows=data))
   c.close()
   # Рядок, в якому викликається view для форматування.
   # Це викликає шаблон (view) з ім'ям bring_to_picnic.tpl
   # для форматування даних. Він передає змінну  data в якості змінної шаблона `rows`
   output = template('bring_to_picnic', rows=list(data)) #bring_to_picnic.tpl
   return output
   # return dict(rows=data) # Повернення форматованого  виведення в браузері на запит користувача у форматі словника

run(host='localhost', port=8089, reloader=True)

