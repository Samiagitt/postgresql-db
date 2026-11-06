
from credentials import connection

conn = None
cur = None

try:
    conn = connection()
    cur = conn.cursor()
    query = "SELECT * FROM employee"
    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

except Exception as error:
    print("Error:", error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()