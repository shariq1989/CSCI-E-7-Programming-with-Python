import csv
import psycopg2
from db.config import config, MyDatabase


def test_connection():
    # Connect to the PostgreSQL database server
    conn = None
    try:
        version = [
            ('PostgreSQL 12.3 on x86_64-pc-linux-gnu, compiled by gcc (GCC) 4.8.3 20140911 (Red Hat 4.8.3-9), 64-bit',)
        ]
        db = MyDatabase()
        # display the PostgreSQL database server version
        db_version = db.query_fetch("SELECT version()")
        db.close()
        assert db_version == version, 'DB conn failed'
        print('DB connection tested successfully')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


test_connection()


def read_csv():
    with open('links.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            print(row[0])
            line_count += 1
        print(f'Processed {line_count} lines.')
