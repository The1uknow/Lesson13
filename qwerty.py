import sqlite3

q = sqlite3.connect("firstbase.db")
cursor = q.cursor()
cursor.execute("DELETE FROM movies")


cursor.execute('''
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    year INTEGER,
    genre TEXT
)
''')

q.commit()


cursor.execute("INSERT INTO movies (title, year, genre) VALUES (?, ?, ?)", ("Inception", 2010, "Sci-Fi"))
cursor.execute("INSERT INTO movies (title, year, genre) VALUES (?, ?, ?)",  ("Interstellar", 2014, "Sci-Fi"))
cursor.execute("INSERT INTO movies (title, year, genre) VALUES (?, ?, ?)", ("The Godfather", 1972, "Crime"))
q.commit()

cursor.execute("SELECT * FROM movies")
rows = cursor.fetchall()
for r in rows:
    print(rows)


cursor.execute("UPDATE movies SET genre = ? WHERE title = ?", ("Drama", "The Godfather"))
q.commit()


cursor.execute("DELETE FROM movies WHERE title = ?", ("Inception",))
q.close()