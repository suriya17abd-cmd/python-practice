import sqlite3
connection=sqlite3.connect("learning.db")
cursor=connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Tasks(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
status TEXT NOT NULL
)
""")
cursor.execute("DELETE FROM tasks")
cursor.executemany(
    "INSERT INTO tasks(title,status)VALUES(?,?)",
    [
        ( "learn sql","pending"),
        ("python","pending")
    ]
)
connection.commit()
print("all tasks")
cursor.execute("SELECT title,status FROM tasks")
for task in cursor.fetchall():
    print(task)
cursor.execute("UPDATE tasks SET status=? WHERE title=?",
               ("complete","learn sql"))
connection.commit()
print("\nAfter update:")
cursor.execute("SELECT title,status FROM tasks")
for task in cursor.fetchall():
    print(task)
cursor.execute("DELETE FROM tasks WHERE title=?",
               ("learn sql",)
               )
connection.commit()
print("\nAfter delete")
cursor.execute("SELECT title,status FROM tasks")
for task in cursor.fetchall():
    print(task)
connection.close()
