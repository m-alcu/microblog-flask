from app import flask_app
from sqlalchemy.sql import text
from sqlalchemy import create_engine
from config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

with engine.connect() as con:

    data = ( { "id": 1, "username": "username 1", "email": "user1@email.com", "password_hash": "pass_bla_bla" },
             { "id": 2, "username": "username 2", "email": "user2@email.com", "password_hash": "pass_bla_bla" },
             { "id": 3, "username": "username 3", "email": "user3@email.com", "password_hash": "pass_bla_bla" },
             { "id": 4, "username": "username 4", "email": "user4@email.com", "password_hash": "pass_bla_bla" },
             { "id": 5, "username": "username 5", "email": "user5@email.com", "password_hash": "pass_bla_bla" },
             { "id": 6, "username": "username 6", "email": "user6@email.com", "password_hash": "pass_bla_bla" },
             { "id": 7, "username": "username 7", "email": "user7@email.com", "password_hash": "pass_bla_bla" },
             { "id": 8, "username": "username 8", "email": "user8@email.com", "password_hash": "pass_bla_bla" },
             { "id": 9, "username": "username 9", "email": "user9@email.com", "password_hash": "pass_bla_bla" },
             { "id": 10, "username": "username 10", "email": "user10@email.com", "password_hash": "pass_bla_bla" },
             { "id": 11, "username": "username 11", "email": "user11@email.com", "password_hash": "pass_bla_bla" },
    )

    statement = text("""INSERT INTO user(id, username, email, password_hash) VALUES(:id, :username, :email, :password_hash)""")

    for line in data:
        con.execute(statement, **line)

    data = ( { "id": 1, "body": "Fisrt Post", "timestamp": "2019-10-10 06:41:45.189000", "user_id": "1" },
             { "id": 2, "body": "Another Post", "timestamp": "2019-10-10 06:41:45.189000", "user_id": "1" },
             { "id": 3, "body": "Another Post", "timestamp": "2019-10-10 06:41:45.189000", "user_id": "1" },
             { "id": 4, "body": "Another Post", "timestamp": "2019-10-10 06:41:45.189000", "user_id": "1" },
             { "id": 5, "body": "Another Post", "timestamp": "2019-10-10 06:41:45.189000", "user_id": "1" },
             { "id": 6, "body": "Another Post", "timestamp": "2019-10-10 06:41:45.189000", "user_id": "1" },
             { "id": 7, "body": "Another Post", "timestamp": "2019-10-10 06:41:45.189000", "user_id": "1" },
             { "id": 8, "body": "Another Post", "timestamp": "2019-10-10 06:41:45.189000", "user_id": "1" },
             { "id": 9, "body": "Another Post", "timestamp": "2019-10-10 06:41:45.189000", "user_id": "1" },
             { "id": 10, "body": "Another Post", "timestamp": "2019-10-10 06:41:45.189000", "user_id": "1" },
             { "id": 11, "body": "Another Post", "timestamp": "2019-10-10 06:41:45.189000", "user_id": "1" },
             { "id": 12, "body": "Another Post", "timestamp": "2019-10-10 06:41:45.189000", "user_id": "1" },
             { "id": 13, "body": "Another Post", "timestamp": "2019-10-10 06:41:45.189000", "user_id": "1" },
             { "id": 14, "body": "Another Post", "timestamp": "2019-10-10 06:41:45.189000", "user_id": "1" },
             { "id": 15, "body": "Another Post", "timestamp": "2019-10-10 06:41:45.189000", "user_id": "1" },
             { "id": 16, "body": "Another Post", "timestamp": "2019-10-10 06:41:45.189000", "user_id": "1" },
             { "id": 17, "body": "Another Post", "timestamp": "2019-10-10 06:41:45.189000", "user_id": "1" },
             { "id": 18, "body": "Another Post", "timestamp": "2019-10-10 06:41:45.189000", "user_id": "1" },
             { "id": 19, "body": "Another Post", "timestamp": "2019-10-10 06:41:45.189000", "user_id": "1" },
             { "id": 20, "body": "Another Post", "timestamp": "2019-10-10 06:41:45.189000", "user_id": "1" },
    )

    statement = text("""INSERT INTO post(id, body, timestamp) VALUES(:id, :body, :timestamp)""")

    for line in data:
        con.execute(statement, **line)