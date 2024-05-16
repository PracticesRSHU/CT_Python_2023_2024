# Subquery Operators
# 	- [NOT] EXISTS				  - повертає TRUE якщо запит повернув хоча б один запис
# 	- [> < >= <= <> =] ANY / SOME - повертає TRUE якщо хоча б одни запис відповідає умові
# 	- [> < >= <= <> =] ALL		  - повертає TRUE якщо всі записи відповідають умові
# 


# /********** Загальний шаблон запиту
# 	SELECT що саме
# 	FROM звідки
# 	додаткові параметри запиту (фільтрація, сортування...)

# 	SELECT колонка1, колонка2
# 	FROM таблиця1
# 	WHERE умова фільтрації
# 	ORDER BY ключ сортування


# Logical operators: 
# 		> <		більше / менше
# 		>= <=	більше рівне / менше рівне
# 		<> =	не  / дорівнює
# 		!> !<	не більше / не менше
# 		IS NULL / IS NOT NULL
# 		BETWEEN / IN
# 		LIKE

# 	negative: NOT
# 	logical and(&&): AND
# 	logical or(||):  OR


# /********** Функції для отримання значення дати
# 	DAY(date) - повертає день з дати
# 	MONTH(date) - повертає день з дати
# 	YEAR(date) - повертає день з дати 
# */

# /******** [value] IN (value1, value2...) - перевіряє на рівність значення [value] з одним в дужках **********/

# #/******** [value] LIKE 'pattern' - перевіряє значення [value] на відповідність шаблону
# 	%	- будь-яка кількість символів
# 	_	- будь-який один символ
# 	[]	- будь-який символ, який наявний в дужках
# 	[^]	- будь-який символ, який НЕ наявний в дужках
# */


import sqlite3
#CRUD create (insert) , read (select), update (update), delete (delete)
# import pandas as pd
#приклад використання модуля os для роботи з файлами
# import os
# db_file=os.getcwd()+'\ishop.db' #отримати повний шлях до файла бази даних
# print(db_file)
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# my_file = os.path.join(BASE_DIR, 'ishop.db')
# print(my_file)

conn = sqlite3.connect('techshop.db')
curs = conn.cursor()
curs.execute('''SELECT * FROM computers WHERE name LIKE 'Note%' ''')
conn.commit()
rows = curs.fetchall()
print(len(rows))
print(type(rows))
for row in rows:
    print(row)
    print("id: ", row[0]," marka: ", row[1]," count: ", row[2], " price: ",row[3])
curs.close()
conn.close()

#вибірка з однієї таблиці
# conn = sqlite3.connect("techshop.db")
# curs = conn.cursor()
# curs.execute("DELETE FROM computers WHERE price>11000")
# conn.commit()
# curs.close()
# conn.close()

# pd.options.display.max_columns=10
#
# # вибірка з кількох таблиць
# conn = sqlite3.connect('techshop.db')
# curs = conn.cursor()
# curs.execute('''SELECT  o.id, o.date_order, u.firstname, c.name,c.price 
#                 FROM orders as o
#                 JOIN users as u ON u.id=o.user_id
#                 JOIN computers as c ON c.id=o.computers_id ;''')
# # print(pd.read_sql('''SELECT  o.id, o.date_order, u.secondname, c.name,c.price FROM  orders as o
# #                 JOIN users as u ON u.id=o.user_id
# #                 JOIN computers as c ON c.id=o.computers_id
# #                 WHERE o.id=2;''',conn))
# conn.commit()
# rows = curs.fetchall()
# print(len(rows))
# print(rows)
# for row in rows:
#     print("id order: ", row[0], "date: ",row[1], "users: ",row[2], "product: ", row[3]," price: ",row[4])
# curs.close()
# conn.close()

# # вибірка з таблиці users
# # conn = sqlite3.connect('techshop.db')
# # curs=conn.cursor()
# # curs.execute("SELECT * FROM users")
# # result_users=curs.fetchmany(2)
# # print(result_users)
# # curs.close()
# # conn.close()