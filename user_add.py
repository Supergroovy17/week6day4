# 1. Add a new user...done
# 2. View user details...done
# 3. Display all users...done
    
from db_connection import connect_db
from user_fetch import fetch_all_users
from mysql.connector import Error
def add_user():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            name = input("What is your name? ").title()
            email = int(input("What is your email "))
          

            new_user = (name, email, )

            query = "INSERT INTO books (name, email, ) VALUES (%s, %s)"

            cursor.execute(query, new_user)
            conn.commit() #fully commits the changes
            print(f" {name} added successfully!")
        
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()