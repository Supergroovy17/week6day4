# 1. Add a new book ...done but fetch all books is not reachable
# 2. Borrow a book ...
# 3. Return a book...
# 4. Search for a book...done
# 5. Display all books...done


from db_connection import connect_db
from mysql.connector import Error

def add_book():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            title = input("What is the title? ").title()
            isbn = int(input("What is the isbn? "))
            publication_date = int(input('What is the publication_date?'))
            availability = input('What is the availability? (True/False): ').lower()  
            availability_bool = availability == 'true'  
            availability_int = int(availability_bool)

            new_book = (title, isbn, publication_date, availability_int)

            query = "INSERT INTO books (title, isbn, publication_date, availability) VALUES (%s, %s,%s, %s)"

            cursor.execute(query, new_book)
            conn.commit() 
            print(f" {title} added successfully!")
        
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()