import pymysql

Conn = pymysql.connect(host="127.0.0.1",
                       user="root",
                       password="toor",
                       db="libme",
                       cursorclass=pymysql.cursors.DictCursor)

Cur = Conn.cursor()

def Create_Table(tblname,*cols):
    if Cur.execute("SHOW TABLES") == 0:
        placeholder = "{col}"
        # placeholders = ', '.join(placeholder for unused in cols)
        sql = """CREATE TABLE IF NOT EXISTS {tbl} (""" + placeholder + ")"
        Cur.execute(sql.format(tbl=tblname, col=cols[0]))
    elif tblname in(Cur.fetchall()[0].values()):
        return None

    for i in cols[1:]:
        sql = "ALTER TABLE {tbl} ADD {col}"
        Cur.execute(sql.format(tbl=tblname, col=i))

def Insert_Table(tblname,*rowVals):
    placeholder = "%s"
    placeholders = ', '.join(placeholder for unused in rowVals)

    Cols = """SHOW COLUMNS FROM {tbl}""".format(tbl=tblname)
    Cur.execute(Cols)
    Process = Cur.fetchall()
    Cols = []
    for i in Process:
        Cols.append(i["Field"])

    column = "%s"
    columns = ', '.join(column for unused in Cols[1:])

    sql = "INSERT INTO {tbl} (" + columns + ") VALUES (" + placeholders + ")"
    print(sql, *(*Cols, *rowVals))
    Cur.execute(sql.format(tbl=tblname),*(*Cols, *rowVals))


Create_Table("Testy","id INT(9) unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY", "item VARCHAR(50) NOT NULL", "quantity INT(3) unsigned NOT NULL", "price FLOAT(8,2) unsigned NOT NULL")
Insert_Table("Testy", "Digital Binary Clock",5,250.00)

#sql = "INSERT INTO store (" \
#      "`item`, `quantity`, `price`)" \
#      "VALUES ('Digital Binary Clock', 5, 250.00)"

Conn.commit()
Conn.close()