import mysql.connector


def fetch_column_data():
    # connect to MySQL database
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='edge1'
    )

    # create a cursor to execute SQL statements
    cursor = conn.cursor()

    query = f'''select name from users'''

    # Create a new database
    cursor.execute(query)
    column_values = [row[0] for row in cursor.fetchall()]
    conn.close()

    return column_values


data = fetch_column_data()
# print all column values
print(data)

# print specific column values
print(data[len(data) - 1])
