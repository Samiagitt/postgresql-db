from credentials import connection  #got the connection 

conn=None
cur=None

try:
    conn=connection()
    
    if conn is not None:
        cur=conn.cursor()
        script='''CREATE TABLE IF NOT EXISTS employee(
                  id int PRIMARY KEY,
                  name varchar(40) NOT NULL,
                  salary int,
                  dept_id varchar(30)
            )'''
        cur.execute(script)
        conn.commit()
        print("Table created Successfully")
except Exception as e:
    if conn is not None:
        print("Connected to:", conn.info.dbname)
        conn.close()
        print(e)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()