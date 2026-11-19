import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Find students with marks above 80
cursor.execute("""
SELECT * FROM students
WHERE marks > 80
ORDER BY marks DESC
""")

data = cursor.fetchall()

for student in data:
    print(student)

conn.close()