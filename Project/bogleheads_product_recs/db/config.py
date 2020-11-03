"""
From https://www.postgresqltutorial.com/postgresql-python/connect/
for connecting to a database using a configuration file
"""
from configparser import ConfigParser

import psycopg2


class MyDatabase:
    def __init__(self):
        # read connection parameters and connect
        params = config()
        self.conn = psycopg2.connect(**params)
        # create a cursor
        self.cur = self.conn.cursor()

    def query_fetch(self, query):
        # execute a statement
        self.cur.execute(query)
        return self.cur.fetchall()

    def close(self):
        # close the communication with the PostgreSQL
        self.cur.close()
        self.conn.close()


def config(filename='database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db
