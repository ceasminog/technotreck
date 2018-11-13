import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

import fill_table
import add_data
import work_with_tab

# decorator to work with db
def connect_cursor(f):
    def wrapper(*args, **kwargs):
        try:
            connection = psycopg2.connect(
            user="piscenco", password="quack",
            host="127.0.0.1", database="quack"
            )
            cursor = connection.cursor()
            res = f(cursor, *args, **kwargs)
        except psycopg2.Error as error:
             print("Error : ", error)
        finally:
            if (connection):
                 connection.close()
    return res





@connect_cursor
def db_search_users(cursor, ni):
    find_nick(cursor, ni)


