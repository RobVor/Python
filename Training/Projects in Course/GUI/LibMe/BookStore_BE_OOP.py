"""This is the back-end design of our BookStore Application. Design is done in tkinter/PAGE

The BookStore application store:
Title; Author; Year and ISBN of books saved in the application.

This connects to local SQLite3 database. The Database allows the user to:
View all; Search; Add; Update; Delete records.

Finally we will close the application using the close function."""

import sqlite3

class DBInterface:

    def __init__(self):
        self.conn = sqlite3.connect("Books.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS tblBooks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT UNIQUE NOT NULL, author TEXT NOT NULL, year INTEGER NOT NULL, isbn INTEGER NOT NULL)")
        self.conn.commit()

    def Insert(self,title, author, year, isbn):
        try:
            self.cur.execute("INSERT INTO tblBooks VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
            self.conn.commit()
        except sqlite3.Error:
            self.conn.interrupt()
            print("Cannot insert record, record already exists")
            print("INSERT INTO tblBooks VALUES (NULL,{},{},{},{})".format(title,author,year,isbn))
            print("\n")

    def ViewAll(self):
        self.cur.execute("SELECT * FROM tblBooks")
        records = self.cur.fetchall()
        return records

    def Search(self,title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM tblBooks WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        records = self.cur.fetchall()
        return records

    def Delete(self,id):
        self.cur.execute("DELETE FROM tblBooks WHERE id=?",(id,))
        self.conn.commit()

    def Update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE tblBooks SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()