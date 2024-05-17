import sqlite3

def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn):
    sql_create_books_table = """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER,
        isbn TEXT
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql_create_books_table)
    except sqlite3.Error as e:
        print(e)

def init_db(db_file):
    conn = create_connection(db_file)
    if conn is not None:
        create_table(conn)
    conn.close()

if __name__ == "__main__":
    init_db("library.db")
