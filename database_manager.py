import sqlite3 as sq
import json


class DatabaseManager:
    def __init__(self):
        self.con = sq.connect('main.db')
        self.cur = self.con.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            self.con.commit()
        self.con.close()

    def create_database(self):
        self.cur.executescript("""
        DROP TABLE IF EXISTS days_info;
        CREATE TABLE days_info (
            data_json TEXT
        )
        """)

    def add_data(self, data):
        self.cur.execute("""
        INSERT INTO days_info (data_json)
        VALUES (?)
        """, [json.dumps(data)])

    def get_data(self):
        self.cur.execute("""
        SELECT data_json
        FROM days_info
        """)
        return json.loads(self.cur.fetchone()[0])


if __name__ == '__main__':
    with DatabaseManager() as db:
        db.create_database()
        data = {
            "21.01.2020": {
                "windows": [
                    {
                        1: [True, False, True],
                        2: [True, False],
                        3: [True]
                    },
                    {
                        1: [True, False, True],
                        2: [True, True],
                        3: [True]
                    }
                ],
                "rooms_count": 3,
                "is_correct": True,
                "algorithm_res": [1, 2, 3]
            }
        }
        db.add_data(data)
        print(db.get_data())
