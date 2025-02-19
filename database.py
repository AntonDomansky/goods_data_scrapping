import sqlite3

DB_NAME = 'sqlite_db.db'

# Create new table


def create_db():
    with sqlite3.connect(DB_NAME) as sqlite_conn:
        sql_request = """CREATE TABLE IF NOT EXISTS goods (
                    id INTEGER PIMARY KEY,
                    title TEXT NOT NULL,
                    link TEXT,
                    price REAL,
                    description TEXT,
                    img_link TEXT
                );"""
        sqlite_conn.execute(sql_request)


def record_data(data: dict):
    pass


# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     # sql_requests = "SELECT * FROM courses"
#     sql_requests = "SELECT * FROM courses WHERE reviews_qty>=30"
#     sql_cursor = sqlite_conn.execute(sql_requests)
#     # for record in sql_cursor:
#     #     print(record[1])

#     records = sql_cursor.fetchall()
#     print(records)


# # Add records to the courses table
# courses = [
#     (351, 'JavaScript course', 415, 100),
#     (614, 'C++ course', 161, 10),
#     (721, 'Java Full course', 100, 35)
# ]
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
#     for course in courses:
#         sqlite_conn.execute(sql_request, course)
#         sqlite_conn.commit()
#     print(f"Изменения успешно сохранены")
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
#     sqlite_conn.execute(sql_request, (251,  'Python course', 100, 30))
#     sqlite_conn.commit()
#     print(f"Изменения успешно сохранены")
if __name__ == '__main__':
    # create_db()
    pass
