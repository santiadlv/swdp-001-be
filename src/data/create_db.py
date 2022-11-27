import sqlite3

con = sqlite3.connect("intersermex.db")
cur = con.cursor()

def create_tables(cursor: sqlite3.Cursor, connection: sqlite3.Connection):
    cursor.execute("""
        CREATE TABLE labels
        (id INTEGER PRIMARY KEY,
        purchase_order INTEGER UNIQUE,
        date DATETIME DEFAULT CURRENT_TIMESTAMP,
        description TEXT,
        client TEXT,
        quantity INTEGER,
        supplier TEXT)
    """)

    cursor.execute("""
        CREATE TABLE templates
        (id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        description INTEGER,
        date INTEGER,
        purchase_order INTEGER,
        supplier INTEGER,
        barcode INTEGER,
        client INTEGER,
        quantity INTEGER,
        t_height TEXT,
        t_width TEXT)
    """)
    connection.commit()

def insert_values(cursor: sqlite3.Cursor, connection: sqlite3.Connection):
    cursor.execute('INSERT INTO labels VALUES (66926209391639, 1000, CURRENT_TIMESTAMP, "Test description 1", "Test client 1", 15, "Supplier 1")')
    cursor.execute('INSERT INTO labels VALUES (40901816366985, 1001, CURRENT_TIMESTAMP, "Test description 2", "Test client 2", 2, "Supplier 2")')
    cursor.execute('INSERT INTO labels VALUES (70620314804158, 1002, CURRENT_TIMESTAMP, "Test description 3", "Test client 3", 30, "Supplier 3")')
    cursor.execute('INSERT INTO labels VALUES (43812953554617, 1003, CURRENT_TIMESTAMP, "Test description 4", "Test client 4", 78, "Supplier 4")')
    cursor.execute('INSERT INTO labels VALUES (49602120810498, 1004, CURRENT_TIMESTAMP, "Test description 5", "Test client 5", 9, "Supplier 5")')
    cursor.execute('INSERT INTO labels VALUES (19399760156812, 1005, CURRENT_TIMESTAMP, "Test description 6", "Test client 6", 1, "Supplier 6")')
    cursor.execute('INSERT INTO labels VALUES (49052060943795, 1006, CURRENT_TIMESTAMP, "Test description 7", "Test client 7", 26, "Supplier 7")')
    cursor.execute('INSERT INTO labels VALUES (68785184807770, 1007, CURRENT_TIMESTAMP, "Test description 8", "Test client 8", 34, "Supplier 8")')
    cursor.execute('INSERT INTO labels VALUES (41050377491734, 1008, CURRENT_TIMESTAMP, "Test description 9", "Test client 9", 5, "Supplier 9")')
    cursor.execute('INSERT INTO labels VALUES (13100553873173, 1009, CURRENT_TIMESTAMP, "Test description 10", "Test client 10", 7, "Supplier 10")')

    cursor.execute("""
        INSERT INTO templates (name, description, date, purchase_order, supplier, barcode, client, quantity, t_height, t_width) 
        VALUES ("Completa", TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, TRUE, "10cm", "15cm")
    """)
    cursor.execute("""
        INSERT INTO templates (name, description, date, purchase_order, supplier, barcode, client, quantity, t_height, t_width) 
        VALUES ("Vacia", FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, "10cm", "15cm")
    """)

    connection.commit()

if __name__ == "__main__":
    create_tables(cursor=cur, connection=con)
    insert_values(cursor=cur, connection=con)
    con.close()
