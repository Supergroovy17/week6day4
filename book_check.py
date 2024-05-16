import mysql.connector 
from mysql.connector import Error
from db_connection import connect_db
from datetime import datetime

def borrow_book(user_id):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            book_title = input("Enter the title of the book you want to borrow: ").title()
            query = "SELECT id FROM books WHERE title = %s"
            cursor.execute(query, (book_title,))
            book_id = cursor.fetchone()
            if book_id:
                borrow_date = datetime.now().date()
                insert_query = "INSERT INTO borrowed_books (user_id, book_id, borrow_date) VALUES (%s, %s, %s)"
                cursor.execute(insert_query, (user_id, book_id[0], borrow_date))
                update_query = "UPDATE books SET availability = 0 WHERE id = %s"
                cursor.execute(update_query, (book_id[0],))
                conn.commit() 
                print("Book borrowed successfully!")
            else:
                print("Book not found.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
 



def return_book(user_id):
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            book_title = input("Enter the title of the book you want to return: ").title()
            query = "SELECT id FROM books WHERE title = %s"
            cursor.execute(query, (book_title,))
            book_id = cursor.fetchone()
            if book_id:
                return_date = datetime.now().date()
                update_query = "UPDATE borrowed_books SET return_date = %s WHERE user_id = %s AND book_id = %s AND return_date IS NULL"
                cursor.execute(update_query, (return_date, user_id, book_id[0]))
                update_query = "UPDATE books SET availability = 1 WHERE id = %s"
                cursor.execute(update_query, (book_id[0],))
                conn.commit() 
                print("Book returned successfully!")
            else:
                print("Book not found.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()              