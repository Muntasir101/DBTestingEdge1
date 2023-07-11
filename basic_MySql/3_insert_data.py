import mysql.connector


def insert_data(table_name, data):
    # connect to MySQL database
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='edge1'
    )

    # create a cursor to execute SQL statements
    cursor = conn.cursor()

    query = f'''
        insert into {table_name}(name,email)
        values(%s,%s)       
        '''

    # Create a new database
    cursor.executemany(query, data)
    print("data inserted successfully.")

    conn.commit()

    conn.close()


dummy_data = [
    ("Alma Ivanyutin", "aivanyutin0@constantcontact.com"),
    ("Wally Schulke", "wschulke1@amazonaws.com"),
    ("Letti Lowdes", "llowdes2@google.co.uk")
]

insert_data('users', dummy_data)
