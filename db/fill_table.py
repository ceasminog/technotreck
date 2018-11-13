import psycopg2


def fill_it(cursor):
    try:

        # statement = films.insert().values(title="Doctor Strange", director="Scott Derrickson", year="2016")
        # cursor.execute(statement)
        cursor.execute('''
                CREATE SCHEMA  IF NOT EXISTS Schema1;
                CREATE TABLE IF NOT EXISTS  Schema1.Users (
              user_id serial PRIMARY KEY,
              name    varchar(255),
              nick    varchar(255),
              avatar  bytea
            );''')
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS  Schema1.Chats (
              chat_id              serial PRIMARY KEY,
              is_group_chat        boolean,
              topic                varchar(255),
              last_read_message_id int
            );''')
        cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Schema1.Messages (
              message_id    serial PRIMARY KEY,
              chat_id       integer REFERENCES Schema1.Chats (chat_id),
              user_id       integer REFERENCES Schema1.Users (user_id),
              content       varchar(255),
              added_at_time time,
              added_at_date date
            );''')
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Schema1.Members (
                  user_id              integer REFERENCES Schema1.Users (user_id),
                  chat_id              integer REFERENCES Schema1.Chats (chat_id),
                  new_messages         integer,
                  last_read_message_id integer REFERENCES Schema1.Messages (message_id)
                );''')
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS  Schema1.Attachments (
              attach_id  serial PRIMARY KEY,
              chat_id    integer REFERENCES Schema1.Chats (chat_id),
              user_id    integer REFERENCES Schema1.Users (user_id),
              message_id integer REFERENCES Schema1.Messages (message_id),
              type_       varchar(255),
              url        varchar(255)
            );''')
        print("tables created sucessfuly")
    except Error as er:
        print("Error wile creating:", er)

