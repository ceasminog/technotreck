import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

import fill_table
import add_data
import work_with_tab

try:
    connection = psycopg2.connect(
        user="piscenco", password="quack",
        host="127.0.0.1", database="quack"
    )
    cursor = connection.cursor()
    # test connection
    cursor.execute("SELECT version();")
    row = cursor.fetchone()
    print("You are connected to   - ", row, '\n')
    # create tables if needed
    fill_table.fill_it(cursor)
    # add data
    add_data.addperson(cursor, 'jack', 'frost')
    add_data.addperson(cursor, 'MP', 'ceasminog')
    add_data.addperson(cursor, 'Anna', 'qwerty')
    add_data.addperson(cursor, 'Denis', 'Batoidea1245')
    # commands
    work_with_tab.find_nick(cursor, 'ceasminog')
    work_with_tab.create_a_chat(cursor, False, 'Lets speak')
    work_with_tab.getlist(cursor, 1)


except psycopg2.Error as error:
    print("Error : ", error)
finally:
    if (connection):
        connection.close()
# в конфиг импортировать user = , ...DB_NAME..
# roll back - already is
# shcould write if cinnection is ok
