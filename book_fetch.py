from db_connection import connect_db 
from mysql.connector import Error

def fetch_all_books():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM books;"

            cursor.execute(query)

            for row in cursor.fetchall():
                print(f"{row[0]}.) {row[1]} {row[2]} {row[3]}")
                
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close() 
            conn.close()

def fetch_book():
    conn = connect_db()
    if conn is not None:
        try:
            id = int(input("What is the id of the book you're lookin for?"))
            cursor = conn.cursor()

            query = 'SELECT * FROM books WHERE id = %s'#may need to come back to this I think I messed up 

            cursor.execute(query, (id,))

            row = cursor.fetchall()[0]
            print(f"{row[0]}.) {row[1]} {row[2]} {row[3]}.")
        
        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()
