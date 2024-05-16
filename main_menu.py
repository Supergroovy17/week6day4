from db_connection import connect_db
from book_add import add_book
from book_fetch import fetch_all_books ,fetch_book
from user_add import add_user
from user_fetch import fetch_all_users ,fetch_user
from book_check import borrow_book , return_book 

def main():
    print('Welcome to the Library Management System with Database Integration!')
    while True:
        action = input('''
        1. Book Operations
        2. User Operations
        3. Quit
        ''')
        if action == '1':
            book_main()
        elif action == '2':
            user_menu()
        elif action == '3':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please select again.')

def book_main():
    print('Book Operations')    
    while True:
        action = input('''
1. Add a new book 
2. Borrow a book 
3. Return a book
4. Search for a book
5. Display all books
6. Back to main menu
      ''')
        if action == '1':
            add_book()
        elif action == '2':
            borrow_book()
        elif action == '3':
            return_book()
        elif action == '4':
            fetch_book()
        elif action == '5':
            fetch_all_books()
        elif action == '6':
            break
        else:
            print('Invalid choice. Please select again.')

def user_menu():
    print('User Menu')    
    while True:
        action = input('''
1. Add a new user
2. View user details
3. Display all users
4. Back to main menu
    ''')
        if action == '1':
            add_user()
        elif action == '2':
            fetch_user()
        elif action == '3':
            fetch_all_users()
        elif action == '4':
            break
        else:
            print('Invalid choice. Please select again.')



if __name__ == "__main__":
    main()