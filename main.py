import sqlite3

q = sqlite3.connect("users.db")
cursor = q.cursor()
cursor.execute("DELETE FROM users")

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT
)
''')

cursor.execute("INSERT INTO users VALUES (?, ?)", (1, "Sasha"))
cursor.execute("INSERT INTO users VALUES (?, ?)", (2, "Carlo"))

# cursor.execute("SELECT * FROM users")
# rows = cursor.fetchall()
# for r in rows:
#     print(rows)

# print(cursor.execute("SELECT user_id FROM users").fetchall())

# print(cursor.execute("SELECT * FROM users WHERE user_id = ?", (1,)).fetchone())

# cursor.execute("DELETE FROM users WHERE username = ?", ("Carlo",))


cursor.execute("UPDATE users SET username = ? WHERE user_id = ?", ("Marco", 1))
q.commit()
print(cursor.execute("SELECT * FROM users").fetchall())
