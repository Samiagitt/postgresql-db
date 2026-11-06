
from credentials import connection

conn = None
cur = None

try:
    conn = connection()
    cur = conn.cursor()

    query = """
        DELETE FROM employee
        WHERE name = %s
    """

    data = ('SAM',)

    cur.execute(query, data)
    print("Rows deleted:", cur.rowcount)

    conn.commit()
    print("Successfully deleted!")

except Exception as error:
    if conn is not None:
        conn.rollback()
    print("Error:", error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
