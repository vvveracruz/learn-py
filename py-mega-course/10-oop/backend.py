import sqlite3 as sq

class Database:
    def __init__( self, db ):
        #   executed everytime you call an instance
        self.conn = sq.connect( db )
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS book ( id INTEGER PRIMARY KEY, title text, author text, year integer, ISBN integer ) " )
        self.conn.commit()

    def insert( self, title, author, year, ISBN ):
        self.cur.execute(
            "INSERT INTO book VALUES ( NULL, ?, ?, ?, ? )",
            ( title, author, year, ISBN ) )
        self.conn.commit()

    def view( self ):
        self.cur.execute( "SELECT * FROM book" )
        rows = self.cur.fetchall()
        return rows

    def search( self, title="", author="", year="", ISBN="" ):
        self.cur.execute(
            "SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR ISBN = ?",
            (title, author, year, ISBN ) )
        rows = self.cur.fetchall()
        return rows

    def delete( self, id ):
        self.cur.execute(
            "DELETE FROM book WHERE id = ?",
            (id, ) )
        self.conn.commit()

    def update( self, id, title, author, year, ISBN ):
        self.cur.execute(
            "UPDATE book SET title = ?, author = ?, year = ?, ISBN = ? WHERE id = ?",
            ( title, author, year, ISBN, id ) )
        self.conn.commit()

    def __del__(self):
        #   executed when the script is exited (the instance is deleted)
        self.conn.close()
