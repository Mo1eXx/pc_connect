import sqlite3
from contextlib import contextmanager
import re


my_list = {}

with open('all_pc.txt', 'r') as file:
    content = file.read()
    list_content = re.split('\n', content)

    for i in list_content:
        pc_name = re.split(': ', str(i))
        my_list[pc_name[0]] = pc_name[-1]



@contextmanager
def sqlite_conn(db_path):
    conn = sqlite3.connect(db_path)
    #conn.row_factory = sqlite3.Row

    try:
        yield conn

    finally:
        conn.close()


if __name__=='__main__':
    db_path = 'db.sqlite'

    with sqlite_conn(db_path) as conn:
        sqlite_cursor = conn.cursor()
        sqlite_cursor.execute(
            '''
            DROP TABLE IF EXISTS ENTRIES
            '''
        )
        sqlite_cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS person (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
            );
            '''
        )
        # sqlite_cursor.execute(
        #     '''
        #     CREATE TABLE IF NOT EXISTS pc (
        #         id PRIMARY KEY,
        #         title TEXT
        #         );
        #     '''
        # )
        # sqlite_cursor.execute(
        #     '''
        #     CREATE TABLE IF NOT EXISTS person_pc (
        #         id uuid PRIMARY KEY,
        #         pc_id uuid NOT NULL,
        #         person_id uuid NOT NULL
        #         );
        #     '''
        # )
        # sqlite_cursor.execute(
        #     '''
        #     CREATE INDEX IF NOT EXISTS person_pc_idx ON person_pc (
        #         pc_id,
        #         person_id
        #         );
        #     '''
        # )

        for pc, name in my_list.items():
            sqlite_cursor.execute(
                f'INSERT INTO pc (title) VALUES (?);', (pc, )
            )
            sqlite_cursor.execute(
                f'INSERT INTO person (name) VALUES (?);'
            )

        sqlite_cursor.execute(
            '''
            SELECT * FROM person;
            '''
        )
        users = sqlite_cursor.fetchall()

        print(users)