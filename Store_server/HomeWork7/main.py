import psycopg2
from config import host, user, password, db_name

try:
    # подключение к бд и написание различных запросов к таблицам
    connection = psycopg2.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        password='23Skb4zx.ru',
        database='Psycopg2'
    )
    connection.autocommit = True

    # cursor = connection.cursor()
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")

        # создание новое таблицы в бд
        #  with connection.cursor() as cursor:
        #      cursor.execute(
        #          """CREATE TABLE users(
        #              id serial PRIMARY KEY,
        #              first_name varchar(50) NOT NULL,
        #              nick_name varchar(50) NOT NULL);"""
        #      )

        # connection.commit()
        #     print("[INFO] Table created successfully")

        # заполнение данным столбцы в бд
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO users (first_name, nick_name) VALUES
            ('Adelya', 'Fattakhova');"""
        )
        cursor.commit()

    #     print("[INFO] Data was succefully inserted")

    # get data from a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT nick_name FROM users WHERE first_name = 'Oleg';"""
    #     )

    #     print(cursor.fetchone())

    # delete a table
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DROP TABLE users;"""
    #     )

    #     print("[INFO] Table was deleted")
# обрабатывает ошибки
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
# закрытие соединения, чтобы не кушало ресурсы
finally:
    if connection:
        # cursor.close()
        connection.close()
        print("[INFO] PostgreSQL connection closed")
