import mysql.connector


def fetch_data():
    # connect to MySQL database
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='edge1'
    )

    # create a cursor to execute SQL statements
    cursor = conn.cursor()

    query = f'''select name,email from users'''

    # Create a new database
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    return rows


data = fetch_data()
for row in data:
    print(row)
