import sqlite3
from colorama import Fore, Back, Style

def create_tables(conn):
    conn.execute("DROP TABLE IF EXISTS students")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        city TEXT
    )   
    """)

def add_student(conn, name, age, city):
    conn.execute("""
    INSERT INTO students (name, age, city) 
    VALUES (?, ?, ?)
    """, (name, age, city))
    conn.commit()

def delete_student(conn, student_id):
    conn.execute("""
    DELETE FROM students WHERE id = ?""", (student_id,))
    conn.commit()

def get_all_students(conn):
    # result = conn.execute("""
    # SELECT * FROM students
    # WHERE city = 'Bishkek' AND
    # (age < 20 AND age > 18)
    # """
    # )
    # return result.fetchmany(size=2)
    result = conn.execute("""
    SELECT * FROM students 
    ORDER BY name
    """)
    return result.fetchall()


def get_student(conn, student_id):
    result = conn.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    return result.fetchone()


def change_student(conn, student_id, name):
    conn.execute("""
    UPDATE students SET name = ?, age = 20 WHERE id < 1000 
    """,
     (name,)
    )
    conn.commit()


if __name__ == "__main__":
    conn = sqlite3.connect("database.db")
    create_tables(conn)
    add_student(conn, "Maksat", 19, "Bishkek")
    add_student(conn, "Azamat", 20, "Bishkek")
    add_student(conn, "Edil", 21, "Karakol")
    # delete_student(conn, 3)

    print(get_all_students(conn))
    print(type(get_all_students(conn)))

    print(get_student(conn, 3))
    change_student(conn, 2, 'Maksat')
    print(get_all_students(conn))
    conn.close()


    print("====== colorama ======")
    print(Fore.RED + 'some red text')
    print(Back.GREEN + 'and with a green background')
    print(Style.DIM + 'and in dim text')
    print(Style.RESET_ALL)
    print('back to normal now')
