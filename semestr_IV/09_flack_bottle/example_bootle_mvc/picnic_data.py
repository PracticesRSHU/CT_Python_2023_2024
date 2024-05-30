import sqlite3
db = sqlite3.connect('picnic.db')
db.execute("DROP TABLE IF EXISTS picnic")
db.execute("CREATE TABLE picnic (id INTEGER PRIMARY KEY, item CHAR(100) NOT NULL, counts INTEGER NOT NULL)")
db.execute("INSERT INTO picnic (item,counts) VALUES ('bread', 4)")
db.execute("INSERT INTO picnic (item,counts) VALUES ('cheese', 2)")
db.execute("INSERT INTO picnic (item,counts) VALUES ('grapes', 30)")
db.execute("INSERT INTO picnic (item,counts) VALUES ('cake', 1)")
db.execute("INSERT INTO picnic (item,counts) VALUES ('soda', 4)")
db.commit()

