import mysql.connector


def create_new_database():
    # connect to MySQL database
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password=''
    )

    # create a cursor to execute SQL statements
    cursor = conn.cursor()

    # Create a new database
    cursor.execute('CREATE DATABASE edge1')
    print("Created database successfully.")

    conn.close()


create_new_database()
