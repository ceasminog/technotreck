import psycopg2


def addperson(cursor, new_name, new_nick):
    try:
        # statement = Schema1.Users.insert().values(name=new_name, nick=new_nick)
        # cursor.execute(statement)
        cursor.execute('''
                INSERT INTO Schema1.Users (name, nick)
                VALUES 
                ('{}', '{}');'''.format(new_name, new_nick))
        print("data added sucessfuly")
    except Error as er:
        print("Error wile adding:", er)
