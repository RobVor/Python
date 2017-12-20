import mysql.connector
import logging, os, sys

def CLSC():
    os.system("cls" if os.name == "nt" else "clear")

#DEBUG
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
"""Use this to enable or disable the debuf logging added into the code. Works better than 'print()' command to track what is going on in the code"""
#logging.disable(logging.DEBUG)
#End of DEBUG

#Database server initialization
Conn = mysql.connector.connect(user="root",
                               password="root",
                               host="localhost"
                               )
Cur = Conn.cursor()
#End of database initialization

#Database functions

def ValuePadding(key):
    """This function creates the placeholders for values being fed to the database commands.
    It uses the new string formatting methods to build the placeholders and source the replacement values"""
    return "{}"

def AlterCheck(struct, ops):
    """This function checks the length of the ALTER table construct
    The ALTER construct needs to be split into multiple columns with commas
    after the first 4 (table, operation, column, column definition) parameters
    This will allow multiple Alterations can be done at the same time
    Currently the function limit multiple alterations to 10 with a minimum of one
    and a maximum of ten in a single ALTER construct"""

    lenCheck = [4,6,8,10,12,14,16,18,20,22]
    if len(struct) in lenCheck:
        return ", " + ops
    else:
        return ""

def CreateDatabase(dbname, charset = "CHARACTER SET = utf8mb4", collate = "COLLATE = utf8mb4_general_ci"):
    """Creates a new database. Additionally the default character set and collation are set by the function. This can be changed.
        Refer to the MariaDB/MySQL documentation fro supported character sets and collations."""

    try:
        logging.debug("Creating database")
        # Lets see... Does it exist?
        check = "SHOW DATABASES LIKE '{}';"
        Cur.execute(check.format(dbname))
        check = Cur.fetchall()
        if len(check) == 0:
            # No it doesn't, let's create it
            logging.debug("......Database does not exist")
            logging.debug("......Creating database")
            sql = "CREATE DATABASE IF NOT EXISTS {} {} {};"
            Cur.execute(sql.format(dbname, charset, collate))
            logging.debug("Last statement issued: " + Cur.statement + "\n")
            Cur.execute("USE " + dbname)
        else:
            # Yes it does, not recreating it
            logging.debug("......Database already exists\n")
            Cur.execute("USE " + dbname)
    except mysql.connector.Error as err:
        # Did we pass an incorrect value to the database?
        logging.critical("ERROR IN SQL STATEMENT!")
        logging.critical("LAST ERROR WAS: ")
        logging.critical(err)
        logging.critical("Last statement sent was: ")
        logging.critical(Cur.statement + "\n")
        pass

def CreateTable(tblname, parms):
    """Creates a new table with the name and column(s). Columns are specified as a dictionary/list/tuple when passed to the function"""

    try:
        for i in parms:
            # Are we sending only numeric values as table names? We rather limit it to none.
            # Strings of characters and alphanumerics are allowed.
            if type(i) != str or type(tblname) != str:
                logging.critical("INVALID PARAMETERS PASSED TO CREATE TABLE")
                logging.critical("ONLY STRINGS ARE ACCEPTED AS PARAMETERS")
                sys.exit()

        # Does the table exist?
        logging.debug("Creating table(s)")
        check = "SELECT * FROM information_schema.tables WHERE table_name = '{}';"
        Cur.execute(check.format(tblname))
        check = Cur.fetchall()
        if len(check) == 0:
            # No it doesn't
            logging.debug("......Table does not exist")
            logging.debug("......Creating table")
            if type(parms) == dict:
                # Let's create a table from dict object
                logging.debug(".........Dictionary received with schema definitions")
                logging.debug(".........Converting dictionary")
                # Dictionaries have key value pairs. Here we extract the values.
                # They are what we insert
                newParams = []
                for cols in parms:
                    newParams.append(cols + " " + parms[cols])
                parms = tuple(newParams)
                logging.debug(".........Dictionary converted")
                logging.debug(".........New schema is: " + str(parms) + "\n")

                sql = "CREATE TABLE IF NOT EXISTS {}"
                sql += " ("
                sql += ", ".join(parms)
                sql += ");"
                Cur.execute(sql.format(tblname))
            elif type(parms) == list:
                # Or from a list object
                logging.debug(".........List received")
                logging.debug(".........Converting list")
                parms = tuple(parms)
                logging.debug(".........List converted")
                logging.debug(".........New schema is: " + str(parms) + "\n")

                sql = "CREATE TABLE IF NOT EXISTS {}"
                sql += " ("
                sql += ", ".join(parms)
                sql += ");"
                Cur.execute(sql.format(tblname))
            elif type(parms) == tuple:
                # Or a tuple object
                logging.debug(".........Schema received as tuple")
                logging.debug(".........No conversion required")
                logging.debug(".........Schema is: " + str(parms) + "\n")

                sql = "CREATE TABLE IF NOT EXISTS {}"
                sql += " ("
                sql += ", ".join(parms)
                sql += ");"
                Cur.execute(sql.format(tblname))
            else:
                # If the object passed is none of the above 3, we have a problem...
                logging.critical("INVALID PARAMETERS RECEIVED FOR TABLE CREATE!")
                logging.critical("PLEASE SEND TABLE COLUMN DEFINITIONS AS A DICTIONARY, LIST, OR TUPLE")
                return None
        else:
            # Yes it does
            logging.debug("......Table already exists\n")
    except mysql.connector.Error as err:
        # Did we pass an incorrect value to the database?
        logging.critical("ERROR IN SQL STATEMENT!")
        logging.critical("LAST ERROR WAS: ")
        logging.critical(err)
        logging.critical("Last statement sent was: ")
        logging.critical(Cur.statement + "\n")
        pass

def InsertIntoTable(tblname, parms):
    """This function inserts values into a table. Columns and values can be stated in dictionary/list/tuple for processing"""

    try:
        # Does the table exist that we are inserting into?
        logging.debug("Inserting new values")
        check = "SELECT * FROM information_schema.tables WHERE table_name = '{}';"
        Cur.execute(check.format(tblname))
        check = Cur.fetchall()
        if len(check) == 0:
            # Nope, doesn't seem to. Can't go on with the insert...
            logging.debug("......Table does not exist")
            logging.debug("......Please check the table name or create the table before inserting values")
        else:
            # Yes it does
            if type(parms) == dict:
                # Let's insert some values from a dict object
                logging.debug(".........Dictionary received with schema values")
                logging.debug(".........No conversion required")

                sql = "INSERT INTO {}"
                sql += " ("
                sql += ", ".join(parms)
                sql += ") VALUES ("
                sql += ", ".join(map(ValuePadding,parms))
                sql += ");"

                # Python escapes (correctly) the "'" character, and this throws the Database off when inserting string values.
                # We could double quote the missing characters in and count of Python and Mysql to escape one set... Or we can have the
                # system fix it by itself.
                # This part adds the "'" characters back to string objects
                struct = []
                struct.append(tblname)
                for i in parms:
                    if type(parms[i]) == str:
                        parms[i] = "'" + parms[i] + "'"
                        struct.append(parms[i])
                    else:
                        struct.append(parms[i])
                logging.debug(".........Columns and values are: " + str(parms.keys()) + " <--- " + str(parms.values()) + "\n")
                Cur.execute(sql.format(*struct))
            elif type(parms) == list:
                # Or a list object
                logging.debug(".........List received with schema definitions")
                logging.debug(".........Converting list")

                # The list object only passes values, not the columns as well (might need to change that)
                # This part gets the column names from the table. It assumes that we are sending them through correctly though
                # (Consider changing this to have lists send columns and values ie. ["item","Clock","Quantity",5,"Price",125]
                getCols = "SHOW columns FROM {};"
                Cur.execute(getCols.format(tblname))
                getCols = Cur.fetchall()
                Columns = []
                for i in getCols[1:]: # We are skipping the id column (Assumption)
                    Columns.append(i[0])
                logging.debug(".........List converted")
                logging.debug(".........Columns and values are: " + str(Columns) + " <--- " + str(parms) + "\n")
                # Got the columns, inserting values
                sql = "INSERT INTO {}"
                sql += " ("
                sql += ", ".join(Columns)
                sql += ") VALUES ("
                sql += ", ".join(map(ValuePadding,parms))
                sql += ");"

                # Python escapes (correctly) the "'" character, and this throws the Database off when inserting string values.
                # We could double quote the missing characters in and count of Python and Mysql to escape one set... Or we can have the
                # system fix it by itself.
                # This part adds the "'" characters back to string objects
                struct = []
                struct.append(tblname)
                for i in parms:
                    if type(i) == str:
                        i = "'" + i + "'"
                        struct.append(i)
                    else:
                        struct.append(i)
                Cur.execute(sql.format(*struct))
            elif type(parms) == tuple:
                # Or a tuple object
                logging.debug(".........Values received as tuple")
                logging.debug(".........Converting tuple")

                # The list object only passes values, not the columns as well (might need to change that)
                # This part gets the column names from the table. It assumes that we are sending them through correctly though
                # (Consider changing this to have lists send columns and values ie. ["item","Clock","Quantity",5,"Price",125]
                getCols = "SHOW columns FROM {};"
                Cur.execute(getCols.format(tblname))
                getCols = Cur.fetchall()
                Columns = []
                for i in getCols[1:]: # We are skipping the id column (Assumption)
                    Columns.append(i[0])
                logging.debug(".........Tuple converted")
                logging.debug(".........Columns and values are: " + str(Columns) + " <--- " + str(parms) + "\n")
                # Got the columns, inserting values
                sql = "INSERT INTO {}"
                sql += " ("
                sql += ", ".join(Columns)
                sql += ") VALUES ("
                sql += ", ".join(map(ValuePadding,parms))
                sql += ");"

                # Python escapes (correctly) the "'" character, and this throws the Database off when inserting string values.
                # We could double quote the missing characters in and count of Python and Mysql to escape one set... Or we can have the
                # system fix it by itself.
                # This part adds the "'" characters back to string objects
                struct = []
                struct.append(tblname)
                for i in parms:
                    if type(i) == str:
                        i = "'" + i + "'"
                        struct.append(i)
                    else:
                        struct.append(i)
                Cur.execute(sql.format(*struct))
            else:
                # If the object passed is none of the above 3, we have a problem...
                logging.critical("INVALID PARAMETERS RECEIVED FOR INSERTING VALUES!")
                logging.critical("PLEASE SEND TABLE VALUES AS A DICTIONARY, LIST, OR TUPLE")
                return None
    except mysql.connector.Error as err:
        # Did we pass an incorrect value to the database?
        logging.critical("ERROR IN SQL STATEMENT!")
        logging.critical("LAST ERROR WAS: ")
        logging.critical(err)
        logging.critical("Last statement sent was: ")
        logging.critical(Cur.statement + "\n")
        pass

def AlterTable(tblname, parms, ops):
    """Makes amendments to existing tables. The table name is supplied with a dictionary/list/tuple
    of new or existing columns that need adding, removing or changing
    Operations are:
    - ADD - Add new column(s) to the table
    - DROP - Remove or delete column(s) from a table
    - MODIFY - Change or update column properties in a table
    - CHANGE - Changes the name of a column in a table ***
    - RENAME - Rename a table"""

    try:
        # Does the table exist that we are altering?
        logging.debug("Altering table schema and properties")
        check = "SELECT * FROM information_schema.tables WHERE table_name = '{}';"
        Cur.execute(check.format(tblname))
        check = Cur.fetchall()
        if len(check) == 0:
            # Nope, doesn't seem to. Can't go on with the alter...
            logging.debug("......Table does not exist")
            logging.debug("......Please check the table name or create the table before trying to alter it")
        else:
            # Yes it does
            if type(parms) == dict:
                logging.debug(".........Alterations received as dictionary")
                logging.debug(".........Converting dictionary to ALTER statement")

                # Here we create the single tuple ALTER construct. It is turned into
                # a single construct as this is much easier to feed to the database
                # using the new updated string formatting.
                struct = []
                struct.append(tblname)
                struct.append(ops)
                for i in parms:
                    struct.append(i)
                    struct.append(parms[i])
                    struct.append(AlterCheck(struct,ops))
                struct = tuple(struct)
                # ALTER construct has been created
                logging.debug(".........Dictionary converted")
                logging.debug(".........ALTER construct is: " + str(struct))

                sql = "ALTER TABLE "
                sql += " ".join(map(ValuePadding,struct))
                Cur.execute(sql.format(*struct))
            elif type(parms) == list:
                logging.debug(".........Alterations received as list")
                logging.debug(".........Converting list to ALTER statement")

                # Here we create the single tuple ALTER construct. It is turned into
                # a single construct as this is much easier to feed to the database
                # using the new updated string formatting.
                struct = []
                struct.append(tblname)
                struct.append(ops)
                for i in parms:
                    struct.append(i)
                    struct.append(AlterCheck(struct, ops))
                struct = tuple(struct)

                sql = "ALTER TABLE "
                sql += " ".join(map(ValuePadding, struct))
                print(sql, struct)
    except mysql.connector.Error as err:
        # Did we pass an incorrect value to the database?
        logging.critical("ERROR IN SQL STATEMENT!")
        logging.critical("LAST ERROR WAS: ")
        logging.critical(err)
        logging.critical("Last statement sent was: ")
        logging.critical(Cur.statement + "\n")
        pass

#End of database functions

#Start of program
CLSC()
#Variables
Database = "DBDev"
Table = "sample"

TableColumns = {"id": "INT(9) unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY",
                "item": "VARCHAR(50) NOT NULL UNIQUE",
                "quantity": "INT(3) unsigned NOT NULL",
                "price": "FLOAT(8,2) unsigned NOT NULL"}
TableColumns2 = ["id INT(9) unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY",
                 "item VARCHAR(50) NOT NULL UNIQUE",
                 "quantity INT(3) unsigned NOT NULL",
                 "price FLOAT(8,2) unsigned NOT NULL"]
TableColumns3 = ("id INT(9) unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY",
                 "item VARCHAR(50) NOT NULL UNIQUE",
                 "quantity INT(3) unsigned NOT NULL",
                 "price FLOAT(8,2) unsigned NOT NULL")

TableValues = {"item": "Digital Binary Clock","quantity":5, "price": 250.00}
TableValues2 = ["Digital Binary Clock", 5, 250.00]
TableValues3 = ("Digital Binary Clock", 5, 250.00)
TableValues4 = [("Digital Binary Clock", 5, 250.00),("Analogue Clock", 3, 120.00),("Wrist watch", 5, 350.00)]

TableMod = {"Total": "FLOAT(8,2) unsigned NOT NULL", "Supplier_Stock_Avail": "TINYINT(1) NOT NULL"}
TableMod2 = ("Total", "FLOAT(8,2) unsigned NOT NULL", "Supplier_Stock_Avail", "TINYINT(1) NOT NULL")
TableMod3 = ["Total", "FLOAT(8,2) unsigned NOT NULL", "Supplier_Stock_Avail", "TINYINT(1) NOT NULL"]


CreateDatabase(Database)
CreateTable(Table,TableColumns3)
InsertIntoTable(Table,TableValues)

for i in TableValues4:
    InsertIntoTable(Table,i)

AlterTable(Table,TableMod3,"ADD")

Conn.commit()
Cur.close()
Conn.close()