import psycopg2


def find_nick(cursor, ni):
    # поиск пользователей
    try:
        # statement = Schema1.Users.insert().values(name=new_name, nick=new_nick)
        # cursor.execute(statement)
        cursor.execute('''
                SELECT * FROM Schema1.Users 
                WHERE nick='{}';'''.format(ni))
        print("found ", ni)
    except Error as er:
        print("Error while finding nick:", er)


# создание персонального чата
def create_a_chat(cursor, is_group_chat, topic):
    try:
        cursor.execute('''
                            INSERT INTO Schema1.Chats(is_group_chat, topic)
                            VALUES 
                            
                            ('{}', '{}');'''.format(is_group_chat, topic))
        print('created a chat')
    except Error as er:
        print("Error while finding nick:", er)

def getlist(cursor, pers_id):
    # получение списка чатов
    try:
        cursor.execute('''
                SELECT c.chat_id, c.is_group_chat, c.topic
                FROM Schema1.Chats as c
                INNER JOIN Schema1.Members as m 
                ON c.chat_id = m.chat_id
                Where m.user_id='{}';'''.format(pers_id))
        print("made a list for user with id #",pers_id)
    except Error as er:
        print("Error while getting list :", er)