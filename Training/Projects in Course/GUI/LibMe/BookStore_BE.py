"""This is the back-end design of our BookStore Application. Design is done in tkinter/PAGE

The BookStore application store:
Title; Author; Year and ISBN of books saved in the application.

This connects to local SQLite3 database. The Database allows the user to:
View all; Search; Add; Update; Delete records.

Finally we will close the application using the close function."""

import sqlite3

def Connect():
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tblBooks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT UNIQUE NOT NULL, author TEXT NOT NULL, year INTEGER NOT NULL, isbn INTEGER NOT NULL)")
    conn.commit()
    conn.close()

def Insert(title, author, year, isbn):
    try:
        conn = sqlite3.connect("Books.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO tblBooks VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        conn.commit()
        conn.close()
    except sqlite3.Error:
        conn.interrupt()
        print("Cannot insert record, record already exists")
        print("INSERT INTO tblBooks VALUES (NULL,{},{},{},{})".format(title,author,year,isbn))
        print("\n")
        conn.close()

def ViewAll():
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM tblBooks")
    records = cur.fetchall()
    conn.close()
    return records

def Search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM tblBooks WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    records = cur.fetchall()
    conn.close()
    return records

def Delete(id):
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM tblBooks WHERE id=?",(id,))
    conn.commit()
    conn.close()

def Update(id,title,author,year,isbn):
    conn = sqlite3.connect("Books.db")
    cur = conn.cursor()
    cur.execute("UPDATE tblBooks SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

Connect()