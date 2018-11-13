CREATE SCHEMA Schema1;
CREATE TABLE Schema1.Users (
  user_id integer,
  name    varchar(255) PRIMARY KEY,
  nick    varchar(255),
  avatar  bytea
);

CREATE TABLE Schema1.Members (
  user_id              integer REFERENCES Schema1.Users (user_id),
  chat_id              integer REFERENCES Schema1.Chats (chat_id),
  new_messages         integer,
  last_read_message_id integer REFERENCES Schema1.Messages (message_id)
);

CREATE TABLE Schema1.Chats (
  chat_id              integer,
  is_group_chat        boolean,
  topic                varchar(255),
  last_read_message_id int
);

CREATE TABLE Schema1.Messages (
  message_id    integer PRIMARY KEY,
  chat_id       integer REFERENCES Schema1.Chats (chat_id),
  user_id       integer REFERENCES Schema1.Users (user_id),
  content       varchar(255),
  added_at_time time,
  added_at_date date
);

CREATE TABLE Schema1.Attachments (
  attach_id  integer PRIMARY KEY,
  chat_id    integer REFERENCES Schema1.Chats (chat_id),
  user_id    integer REFERENCES Schema1.Users (user_id),
  message_id integer REFERENCES Schema1.Messages (message_id),
  type       varchar(255),
  url        varchar(255)
);
