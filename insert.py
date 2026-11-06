from credentials import connection
conn=None
cur=None

try:
    conn=connection()
    cur=conn.cursor()
    #query="""INSERT INTO employee(name,salary)
           # VALUES (%s, %s)"""
    #employee=("ALICE",50000)
    #cur.execute(query,employee)
    
    #Multiple insertion
    
    multi_insert='INSERT INTO employee(id, name, salary, dept_id)VALUES(%s,%s,%s,%s)'
    Values=[(2,'James',2000,'D1'),(3,'EMMA',2000,'D1'),(4,'SAM',2000,'D1')]
    cur.executemany(multi_insert,Values)
    conn.commit()
    print("successfully inserted")
except Exception as error:
    if conn is not None:
        conn.rollback()
    print("Error:", error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
    