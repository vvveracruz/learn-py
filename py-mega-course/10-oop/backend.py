import sqlite3 as sq

class Database:
    def __init__( self, db ):
        conn = sq.connect( db )
        cur = conn.cursor()

        cur.execute( "CREATE TABLE IF NOT EXISTS book ( id INTEGER PRIMARY KEY, title text, author text, year integer, ISBN integer ) " )

        conn.commit()

    def insert( self, title, author, year, ISBN ):
        cur.execute( "INSERT INTO book VALUES ( NULL, ?, ?, ?, ? )", ( title, author, year, ISBN ) )

        conn.commit()
        conn.close()

    def view( self ):
        cur.execute( "SELECT * FROM book" )
        rows = cur.fetchall()

        conn.close()

        return rows

    def search( self, title="", author="", year="", ISBN="" ):
        cur.execute( "SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR ISBN = ?", (title, author, year, ISBN ) )
        rows = cur.fetchall()

        conn.close()

        return rows

    def delete( self, id ):
        cur.execute( "DELETE FROM book WHERE id = ?", (id, ) )

        conn.commit()
        conn.close()

    def update( self, id, title, author, year, ISBN ):
        cur.execute( "UPDATE book SET title = ?, author = ?, year = ?, ISBN = ? WHERE id = ?", ( title, author, year, ISBN, id ) )

        conn.commit()
        conn.close()
