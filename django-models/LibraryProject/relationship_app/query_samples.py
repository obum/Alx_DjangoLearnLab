
from mysql.connector import connect, Error

DB_NAME = 'library'

# A function to return a database connection

def create_connection():
    
    a_connection = connect(
        host= "localhost",
        user= "root",
        password= "Stevengerad8!",
        database= DB_NAME )
    return a_connection

def main():
    try:
        connection = create_connection()
        
        if connection and connection.is_connected():
            mycursor = connection.cursor()
            print(f'Database Conncetion Succesful: {connection.get_server_info()}')
            print()
        
    except Error as err:
        print(f'Connection Error: {err.msg}')
        
    else:
        print('Query all books by a specific author.')
        book_query = f"""
            SELECT title 
            FROM relationship_app_book
            WHERE author_id = %s;
                    """
        mycursor.execute(book_query, (4,))
        all_books_ = mycursor.fetchall()
        for book in all_books_:
            print(book[0])
           
        print() 
        print('List all books in a library.')
        library_query = f"""
        SELECT relationship_app_book.title as 'Books in library'
        FROM relationship_app_book
        INNER JOIN relationship_app_library_books
        ON relationship_app_book.id = relationship_app_library_books.book_id
        WHERE relationship_app_library_books.library_id = %s;
                    """
        mycursor.execute(library_query, (5,))
        libs = mycursor.fetchall()
        for lib in libs:
            print(lib[0])
            
        print() 
        print('Retrieve the librarian for a library.')
        librarian_query = f"""
        SELECT relationship_app_librarian.name as 'librarian'
        FROM relationship_app_librarian
        WHERE library_id = %s;
                    """
        mycursor.execute(librarian_query, (5,))
        libs = mycursor.fetchall()
        for lib in libs:
            print(lib[0])

        
        
if __name__ == "__main__":
    main()

    