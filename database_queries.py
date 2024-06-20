import sqlite3

"""Do some query on database"""

# Establish a connection and a cursor
conn = sqlite3.connect("tours.db")
cursor = conn.cursor()

# Query all data
cursor.execute("SELECT * FROM events")
result = cursor.fetchall()
print(result)

# Query all data based on a condition
cursor.execute("SELECT * FROM events WHERE date='2088.12.13'")
result = cursor.fetchall()
print(result)

# Query certain columns based on a condition
cursor.execute("SELECT bandName, date FROM events WHERE city='Tiger city'")
result = cursor.fetchall()
print(result)

# Insert new rows
new_rows = [('Pigeon', 'Pigeon city', '2088.12.15'),
            ('Zebra', 'Zebra city', '2088.12.15')]

cursor.executemany("INSERT INTO events VALUES (?, ?, ?)", new_rows)
conn.commit()
