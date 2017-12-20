import os, sys, logging, sqlite3

#DEBUG
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
os.system('clear')
#logging.disable(logging.DEBUG) """ remember to use logging.exception for traceback and line numbers """

#Database builder
logging.debug('Initializing Databases and connections.')

CONN = sqlite3.connect('base.db')
logging.debug('Database built. File name is base.db')
C = CONN.cursor()
logging.debug('Cursor created under the name C')

#Variables and Constants
logging.debug('Initializing Variables.')

#Classes (And exceptions)
logging.debug('Initializing custom Classes.')

class NoInput():
    pass

#Functions
logging.debug('Initializing custom Functions.')

def CLSC():
    os.system("cls" if os.name == "nt" else "clear")

def CREATE_TABLE():
    logging.debug('Building Database table.')
    C.execute('CREATE TABLE tblFirst(Language VARCHAR, Version REAL, Skill TEXT)')

def INSERT_DATA():
    C.execute('INSERT INTO tblFirst VALUES("Python", 3.4, "Beginner")')
    C.execute('INSERT INTO tblFirst VALUES("Ruby", 2.7, "Beginner")')
    C.execute('INSERT INTO tblFirst VALUES("C", 7.7, "Advance")')
    CONN.commit()

def INSERT_DYN():
    LANG = input('Language? ')
    VER = float(input('Version? '))
    SKILL = input('Level? ')
    C.execute('INSERT INTO tblFirst (Language, Version, Skill) VALUES (?, ?, ?)', (LANG, VER, SKILL))
    CONN.commit()

def GET_DATA():
    SQL = 'SELECT * FROM tblFirst WHERE Skill == "Super"'
    for row in C.execute(SQL):
        print(row)
        print(row[1])

def CUSTOM_DATA():
    WHAT_SKILL = input('What skill level? ')
    SQL = 'SELECT * FROM tblFirst WHERE Skill = ?'
    for row in C.execute(SQL, [(WHAT_SKILL)]):
        print(row)

def LIMIT_DATA():
    SQL = 'SELECT * FROM tblFirst LIMIT 1'
    for row in C.execute(SQL):
        print(row)
        
def UPDATE_DATA():
    SQL = 'UPDATE tblFirst SET Skill = "Ultimate" WHERE Skill = "Super"'
    C.execute(SQL)

def DELETE_DATA():
    SQL = 'DELETE FROM tblFirst WHERE Skill = "Super"'
    C.execute(SQL)
    
#GPIO
logging.debug('Setting up I/O pins.')

#Main
logging.debug('Program main start.')

CREATE_TABLE()
INSERT_DATA()
INSERT_DYN()
GET_DATA()
CUSTOM_DATA()
LIMIT_DATA()
UPDATE_DATA()
DELETE_DATA()

#End
logging.debug('Program end and cleanup.')
#CONN.close()
logging.debug('Database has been closed.')
