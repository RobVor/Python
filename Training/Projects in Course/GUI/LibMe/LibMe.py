import pymysql

Conn = pymysql.connect(host="127.0.0.1",
                       user="root",
                       password="root",
                       db="libme",
                       cursorclass=pymysql.cursors.DictCursor)

Cur = Conn.cursor()

def Create_New_Table(tblName, parms):
    """Takes a table name and dictionary/list/tuple object to build a new table"""
    sql = "CREATE TABLE IF NOT EXISTS " + tblName
    sql += " ("
    sql += ", ".join(parms)
    sql += ")"
    print(sql, parms)
    #Cur.execute(sql)

def Alter_Existing_Table(tblName, parms, operation):
    """Makes amendments to existing tables. The table name is supplied with a dictionary/list/tuple
    of new or existing columns that need adding, removing or changing
    Operations are:
    - ADD - Add new column(s) to the table
    - DROP - Remove or delete column(s) from a table
    - MODIFY - Change or update column properties in a table
    - CHANGE - Changes the name of a column in a table ***
    - RENAME - Rename a table"""
    sql = "ALTER TABLE " + tblName
    sql += " " + operation + " "
    sql += " ".join(parms)
    print(sql, parms, operation)
    Cur.execute(sql, parms)
    print(Cur.mogrify(sql))

def Insert_New_Records(tblName, parms):
    """Takes a table name and dictionary/list/tuple object to insert records into a table
    Dictionaries can be used with the Key/Value pairs matching the actual columns of the table
    you wish to insert to. Alternatively, use a list or tuple and the function can get the columns
    by itself. !!!If a dictionary is not used, ensure that the values are in the correct order for
    insert into the correct columns!!!"""

    if type(parms) != dict:
        print("Not a dictionary, lets convert it")
        sql = "SHOW columns FROM " + tblName
        Cur.execute(sql)
        GetCols = Cur.fetchall()
        Columns = {}
        for i,j in enumerate(GetCols[1:]):
            Columns[j["Field"]] = parms[i]
        sql = "INSERT INTO " + tblName
        sql += "( "
        sql += ", ".join(Columns)
        sql += ") VALUES ("
        sql += ", ".join(map(dictValuePad,Columns))
        sql += ")"
        print(sql,parms)
        #Cur.execute(sql, Columns)
    else:
        print("Dictionary received, inserting records")
        sql = "INSERT INTO " + tblName
        sql += "( "
        sql += ", ".join(parms)
        sql += ") VALUES ("
        sql += ", ".join(map(dictValuePad,parms))
        sql += ")"
        print(sql,parms)
        #Cur.execute(sql, parms)
        #print(Cur.mogrify(sql,parms))

def dictValuePad(key):
    return "%(" + str(key) + ")s"

Table = "sample"
TableDef = ("id INT(9) unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY",
            "item VARCHAR(50) NOT NULL",
            "quantity INT(3) unsigned NOT NULL",
            "price FLOAT(8,2) unsigned NOT NULL")
TableVals = {"item": "Digital Binary Clock","quantity":5, "price": 250.00}
TableVals2 = ("Analogue Clock", 3, 99.99)
TableVals3 = ["Wrist watch", 3 , 50.00]
NewColumn = {"Total": "FLOAT(8,2) unsigned NOT NULL"}
NewColumn2 = ("Total","FLOAT(8,2) unsigned NOT NULL")

#Create_New_Table(Table,TableDef)
#Insert_New_Records(Table, TableVals)
#Insert_New_Records(Table, TableVals2)
#Insert_New_Records(Table, TableVals3)
Alter_Existing_Table(Table,NewColumn2, "ADD")

#NewColDef = []
#for i in NewColumn:
#    NewColDef.append(i)
#    NewColDef.append(NewColumn[i])
#print(NewColDef)

#for j in NewColDef:
#    print(j)

Conn.commit()
Conn.close()