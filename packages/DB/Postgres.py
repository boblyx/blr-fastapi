"""
Postgres.py

- For handling connections to postgres.
"""


import psycopg2
import os
env = os.environ

class PGConnection:
    def __init__(self):
        self.conn = psycopg2.connect(
            database="dpdiffusion"
            ,user = "postgres"
            ,host = env["POSTGRES_HOST"]
            ,password = env["POSTGRES_PASSWORD"]
            ,port = env["POSTGRES_PORT"]
            )
        self.cur = self.conn.cursor()

    def close(self):
        self.conn.close()
        self.cur.close()
    pass
