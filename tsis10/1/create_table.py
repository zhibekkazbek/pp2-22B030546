import psycopg2
from config import config

try:
    params = config()
    conn = psycopg2.connect(**params)

    conn.autocommit = True
    with conn.cursor() as cur:
        cur.execute(
            "SELECT version();"
        )
        print(f"Server version: {cur.fetchone()}")

    with conn.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE phonebook(
            first_name VARCHAR(255) NOT NULL,
            phone_number NUMERIC NOT NULL)"""
        )
        print("[INFO]: Table created successfully")  


except (Exception, psycopg2.DatabaseError) as error:
    print(error)

finally:
    if conn:
        conn.close()
        print("[INFO]:PostgreSQL connection closed")