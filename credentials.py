import psycopg2 # pyright: ignore[reportMissingModuleSource]
print("Python file is running!")
hostname = 'localhost'
database = 'first_demo'
username = 'postgres'
pwd = '12345'
port_id = 5432
conn=None
cur=None
def connection():
    try:
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id
        )

        print("Database connected successfully!")
        return conn

    except Exception as error:
        print("Connection failed:", error)
        return None
