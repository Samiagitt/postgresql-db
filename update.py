
from credentials import connection

conn = None
cur = None

try:
    conn = connection()
    cur = conn.cursor()

    query = """
        UPDATE employee
        SET salary = %s
        WHERE name = %s
    """

    data = (2000, 'James')

    cur.execute(query, data)
    print("Rows updated:", cur.rowcount)

    conn.commit()
    print("Successfully updated!")

except Exception as error:
    if conn is not None:
        conn.rollback()
    print("Error:", error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()