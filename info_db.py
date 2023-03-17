import logging
import sqlite3
from pathlib import Path
from sqlite3 import Error

Path("info_database.db")
CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS bin_info (
symbol TEXT,
status TEXT,
);
"""
INSERT_INTO_SQL = """
INSERT INTO bin_info
(symbol,status)
VALUES(1,2);
"""
SELECT_FROM_SQL = """
SELECT * FROM bin_info;
"""

def create_connection(db_file: Path):
        """
        Create db file
        :param db_file: path to db file to create
        :return:
        """
        try:
            conn = sqlite3.connect(db_file)
            logging.info("Connection created successfully !")
            return conn
        except Error as create_conn_err:
            logging.error(create_conn_err)
        return None
def create_table(conn):
        """
        :param conn: Connection to the SQLite database
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(CREATE_TABLE_SQL)
            logging.info(f"Table created successfully !")

        except Error as create_table_err:
            logging.error(create_table_err)
def insert_into(conn, data: list):
        """
        Insert data to base
        This is the load step in ETL pipeline
        :param conn: Connection to the SQLite database
        :param data:
        :return:
        """
        try:
            cur = conn.cursor()
            cur.execute(INSERT_INTO_SQL, data)
            conn.commit()
            logging.info(f"Data inserted successfully !")
            return cur.lastrowid
        except Error as insert_err:
            logging.error(insert_err)


def get_all_news(conn):
    """
    Query all rows in the bin_info table
    :param conn: Connection to the SQLite database
    :return:
    """
    return conn.cursor().execute(SELECT_FROM_SQL)

if __name__ == '__main__':
    create_connection("info_database.db")
    create_table(create_connection("info_database.db"))