from db_connection import connect_db
from mysql.connector import Error
def fetch_all_users():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = "SELECT * FROM users;"

            cursor.execute(query)

            for row in cursor.fetchall():
                print(f"{row[0]}.) {row[1]} {row[2]}")
                
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close() 
            conn.close()


def fetch_user():
    conn = connect_db()
    if conn is not None:
        try:
            id = input("What is the user id?")
            cursor = conn.cursor()

            query = 'SELECT * FROM users WHERE id = %s'#may need to come back to this I think I messed up 
            
            cursor.execute(query, (id,))

            row = cursor.fetchall()[0]
            print(f"{row[0]}.) {row[1]} {row[2]}.")
        
        except Error as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()
