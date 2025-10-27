import sqlite3

DB_PATH: str = ".db"


def create_table(db_path: str = DB_PATH):
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS books (
                name TEXT,
                author TEXT,
                publication_year INTEGER,
                genre TEXT,
                number_of_pages INTEGER,
                number_of_copies INTEGER
            )
        """)
        conn.commit()


def insert_books(db_path: str = DB_PATH):
    books = [
        ("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 310, 5),
        ("1984", "George Orwell", 1949, "Dystopia", 328, 4),
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction", 281, 3),
        ("cjhdbhj", "Harper Lee", 1960, "Fiction", 281, 3),
        ("bshd", "Harper Lee", 1960, "Fiction", 281, 3),
        ("aodjdufj", "Harper Lee", 1960, "Fiction", 281, 3),
        ("Pride and Prejudice", "Jane Austen", 1813, "Romance", 279, 2),
        ("Moby-Dick", "Herman Melville", 1851, "Adventure", 635, 1),
    ]
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.executemany("""
            INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
            VALUES (?, ?, ?, ?, ?, ?)
        """, books)
        conn.commit()


def delete_book(name: str, db_path: str = DB_PATH):
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM books WHERE name = ?", (name,))
        conn.commit()


def get_books_by_author(author: str, db_path: str = DB_PATH):
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT name, author, publication_year, genre, number_of_pages, number_of_copies
            FROM books
            WHERE author = ?
            ORDER BY name COLLATE NOCASE ASC
        """, (author,))
        rows = cur.fetchall()
        return rows


if __name__ == "__main__":
    create_table()
    insert_books()

    delete_book("1984")
    delete_book("The Hobbit")

    # Пример: получим книги Harper Lee (после удалений она осталась)
    result = get_books_by_author("Harper Lee")
    print("Книги автора Harper Lee:")
    for row in result:
        # row: (name, author, publication_year, genre, number_of_pages, number_of_copies)
        print(f"- {row[0]} ({row[2]}), жанр: {row[3]}, страниц: {row[4]}, копий: {row[5]}")
