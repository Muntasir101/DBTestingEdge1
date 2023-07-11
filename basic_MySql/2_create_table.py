import mysql.connector


def create_new_table():
    # connect to MySQL database
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='edge1'
    )

    # create a cursor to execute SQL statements
    cursor = conn.cursor()

    # Create a new database
    cursor.execute(
        '''
        Create Table users(id INTEGER AUTO_INCREMENT PRIMARY KEY, 
        name VARCHAR(255), 
        email VARCHAR(255))
        ''')
    print("Created table successfully.")

    conn.close()


create_new_table()
