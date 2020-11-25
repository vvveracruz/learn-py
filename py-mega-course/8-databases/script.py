import psycopg2 as sq

#   5 steps to databases in Python
#       1. connect to a database
#       2. create a cursor object to navigate the database
#       3. write an SQL query
#       4. commit changes to the database
#       5. close connection

def create_table():
    #  if there is no file by this name it will be created
    conn = sq.connect("lite.db")
    cur = conn.cursor()

    #   Writing an SQL query to create a database with a given set of cols
    #   if the table doesn't exist
    #   good practice to use capital letters for the SQL query
    cur.execute( "CREATE TABLE IF NOT EXISTS store ( item TEXT, quantity INTEGER, price REAL )" )

    conn.commit()
    conn.close()

def insert( item, quantity, price ):
    conn = sq.connect("lite.db")
    cur = conn.cursor()

    cur.execute( "INSERT INTO store VALUES ( ?, ?, ? )", (item, quantity, price) )

    conn.commit()
    conn.close()

def view():
    conn = sq.connect("lite.db")
    cur = conn.cursor()

    cur.execute( "SELECT * FROM store" )
    data = cur.fetchall()

    # no need for commit since we are just reading
    conn.close()
    return data

def delete( item ):
    conn = sq.connect("lite.db")
    cur = conn.cursor()

    cur.execute( "DELETE FROM store WHERE item = ?", ( item, ) )

    conn.commit()
    conn.close()

def update( item, quantity, price ):
    conn = sq.connect("lite.db")
    cur = conn.cursor()

    cur.execute( "UPDATE store SET quantity = ?, price = ? WHERE item = ?", ( quantity, price, item ) )

    conn.commit()
    conn.close()

print( view() )
