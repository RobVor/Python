import sqlite3

Connection = sqlite3.connect("lite.db")
Cursor = Connection.cursor()
Cursor.execute("CREATE TABLE tblLiteTable (ID)")