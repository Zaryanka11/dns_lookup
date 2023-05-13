import psycopg2
from config import host, user, password, db_name

conn = psycopg2.connect(
    host='127.0.0.1',
    port=5432,
    user='postgres',
    password='23Skb4zx.ru',
    database='Psycopg2'
)

cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS superheroes")

conn.commit()

# создание таблицы бд
cur.execute(  # """ - перенос строки
    """CREATE TABLE superheroes (
    hero_id serial PRIMARY KEY,
    hero_name varchar(50) NOT NULL,
    strength int);"""
)
conn.commit()
print("Таблица успешно создана")

# заполнение таблицы бд
cur.execute(
    """INSERT INTO superheroes (
    hero_name, strength) VALUES
    ('Superman', 100)"""
)

# заполнение таблицы бд
cur.execute(
    """INSERT INTO superheroes (
    hero_name, strength) VALUES
    ('Spider Man', 80)"""
)

cur.execute(
    """INSERT INTO superheroes (
    hero_name, strength) VALUES
    ('Flash', 999)"""  # Флэш может нанести бесконечное кол-во ударов бесконечной силы,
    # потому что может приложить бесконечную массу => лучший во вселенной DC
)

conn.commit()
print("Запись успешно добавлена в таблицу")

# извлечение данных бд
cur.execute(
    """SELECT strength
    FROM superheroes
    WHERE hero_name = 'Flash';"""
)

one_line = cur.fetchone()
print(one_line)

full_fetch = cur.fetchall()
for record in full_fetch:
    print(record)

# удаление всей таблицы
cur.execute(
    """DROP TABLE superheroes; """
)

conn.commit()
print("Таблица успешно удалена")

cur.close(),
conn.close()
