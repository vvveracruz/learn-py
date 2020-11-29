import psycopg2 as sq

# this code is almost exactly the same as the one for sqlite3

_connection_string = "dbname='pythoncourse' user='veracruz' password='admin' host='localhost' port='5432'"

def create_table():
    conn = sq.connect( _connection_string )
    cur = conn.cursor()

    cur.execute( "CREATE TABLE IF NOT EXISTS store ( item TEXT, quantity INTEGER, price REAL )" )

    conn.commit()
    conn.close()

def insert( item, quantity, price ):
    conn = sq.connect( _connection_string )
    cur = conn.cursor()

    cur.execute( "INSERT INTO store VALUES ( %s,%s,%s )", (item, quantity, price) )

    conn.commit()
    conn.close()

def view():
    conn = sq.connect( _connection_string )
    cur = conn.cursor()

    cur.execute( "SELECT * FROM store" )
    data = cur.fetchall()

    # no need for commit since we are just reading
    conn.close()
    return data

def delete( item ):
    conn = sq.connect( _connection_string )
    cur = conn.cursor()

    cur.execute( "DELETE FROM store WHERE item = %s", ( item, ) )

    conn.commit()
    conn.close()

def update( item, quantity, price ):
    conn = sq.connect( _connection_string )
    cur = conn.cursor()

    cur.execute( "UPDATE store SET quantity = %s, price = %s WHERE item = %s", ( quantity, price, item ) )

    conn.commit()
    conn.close()


insert(  "Orange", 10, 3.45)
update( "Orange", 5, 5 )
print( view() )
