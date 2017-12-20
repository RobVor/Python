"""This is the front-end design of our BookStore Application. Design is done in tkinter/PAGE

The BookStore application store:
Title; Author; Year and ISBN of books saved in the application.

This connects to local SQLite3 database. The Database allows the user to:
View all; Search; Add; Update; Delete records.

Finally we will close the application using the close function."""

import tkinter as tk
from BookStore_BE_OOP import DBInterface

dbs = DBInterface()

window=tk.Tk()
window.wm_title("Book Store")
window.resizable(False,False)

# Commands and Functions
def cmdView():
    lstViewAll.delete(0,tk.END)
    for row in dbs.ViewAll():
        lstViewAll.insert(tk.END,row)

def cmdSearch():
    lstViewAll.delete(0, tk.END)
    for row in dbs.Search(titleText.get(),authorText.get(),yearText.get(),isbnText.get()):
        lstViewAll.insert(tk.END,row)

def cmdInsert():
    lstViewAll.delete(0, tk.END)
    dbs.Insert(titleText.get(),authorText.get(),yearText.get(),isbnText.get())
    lstViewAll.insert(tk.END,(titleText.get(),authorText.get(),yearText.get(),isbnText.get()))

def getSelection(event):
    global selected_row
    try:
        index = lstViewAll.curselection()[0]
        selected_row = lstViewAll.get(index)
        txtTitle.delete(0,tk.END)
        txtTitle.insert(0,selected_row[1])
        txtAuthor.delete(0,tk.END)
        txtAuthor.insert(0,selected_row[2])
        txtYear.delete(0,tk.END)
        txtYear.insert(0,selected_row[3])
        txtISBN.delete(0,tk.END)
        txtISBN.insert(0,selected_row[4])
    except IndexError:
        pass

def cmdDelete():
    dbs.Delete(selected_row[0])
    lstViewAll.delete(0, tk.END)
    for row in dbs.ViewAll():
        lstViewAll.insert(tk.END, row)

def cmdUpdate():
    dbs.Update(selected_row[0],titleText.get(),authorText.get(),yearText.get(),isbnText.get())

# Labels
lblTitle = tk.Label(window,text="Title")
lblTitle.grid(row=0,column=0)

lblYear = tk.Label(window,text="Year")
lblYear.grid(row=1,column=0)

lblAuthor = tk.Label(window,text="Author")
lblAuthor.grid(row=0,column=2)

lblISBN = tk.Label(window,text="ISBN")
lblISBN.grid(row=1,column=2)

# Text input fields for each label
titleText = tk.StringVar()
txtTitle = tk.Entry(window,textvariable=titleText)
txtTitle.grid(row=0,column=1)

yearText = tk.StringVar()
txtYear = tk.Entry(window,textvariable=yearText)
txtYear.grid(row=1,column=1)

authorText = tk.StringVar()
txtAuthor = tk.Entry(window,textvariable=authorText)
txtAuthor.grid(row=0,column=3)

isbnText = tk.StringVar()
txtISBN = tk.Entry(window,textvariable=isbnText)
txtISBN.grid(row=1,column=3)

# Listbox to display all the values
lstViewAll = tk.Listbox(window,height=8,width=35)
lstViewAll.grid(row=2,column=0,rowspan=8,columnspan=2)
scroll = tk.Scrollbar(window)
scroll.grid(row=2,column=2,rowspan=8)
lstViewAll.configure(yscrollcommand=scroll.set)
scroll.configure(command=lstViewAll.yview)
# Bind listbox function selection to return a selected set of information and records.
lstViewAll.bind("<<ListboxSelect>>",getSelection)

# Function buttons
btnViewAll = tk.Button(window,text="View All", width=12,command=cmdView)
btnViewAll.grid(row=2,column=3)

btnSearch = tk.Button(window,text="Search entry",width=12,command=cmdSearch)
btnSearch.grid(row=3,column=3)

btnAdd = tk.Button(window,text="Add entry", width=12,command=cmdInsert)
btnAdd.grid(row=4,column=3)

btnUpdate = tk.Button(window,text="Update entry",width=12,command=cmdUpdate)
btnUpdate.grid(row=5,column=3)

btnDelete = tk.Button(window,text="Delete entry",width=12,command=cmdDelete)
btnDelete.grid(row=6,column=3)

btnClose = tk.Button(window,text="Close",width=12,command=window.destroy)
btnClose.grid(row=7,column=3)



window.mainloop()