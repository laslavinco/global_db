# coding=utf-8
import sqlite3

class DBFunctions(object):


    def __init__(self,db_name):
        self.db = db_name
        self.db = self.db.split('.')[0]
        self.connection = sqlite3.connect(db_name)
        self.connection.text_factory = str
        self.c = self.connection.cursor()

    def make_table(self,tables,*args):
        args = str(args[0])
        self.c.execute('CREATE TABLE IF NOT EXISTS ' + tables+ ' (' + args+' )')

    def write_db(self,table,*args):
        args = str(args[0])
        self.c.execute('INSERT INTO '+ table + args)
        self.connection.commit()


    def read_db(self,table,*args):
        if args:
            args = str(args[0])
        else:
            args = '*'
        if not 'WHERE' in args:
            print ('SELECT '+args+ ' FROM ' + table)
            self.c.execute('SELECT '+args+ ' FROM ' + table)
        else:
            print ('SELECT * FROM ' + table+ ' ' + args)
            self.c.execute('SELECT * FROM ' + table+ ' ' + args)
        data = self.c.fetchall()
        return data

    def update_db(self,table,column,data,where_val):

        self.c.execute('UPDATE ' + table + ' SET ' + column + ' = ' + data + ' WHERE ' + where_val)
        self.connection.commit()

    def close_db(self):
        self.c.close()
        self.connection.close()


'''
Usage :

db_object = DBFunctions('temp_db.db')

db_object.make_table('errorlogger','Filename TEXT, Filesize INTEGER, File_downloaded INTEGER, Error TEXT')

(db_object.write_db('temp_db',' (Filename, Filesize , downloaded , Error) VALUES ("test","temp","xxx","zzzz")'))

'''


