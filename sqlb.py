import sqlite3

conn = sqlite3.connect("new.db")

cursor = conn.cursor()

cursor.execute("insert into population values('New York City', 'NY', 8200000)")
cursor.execute("insert into population values('Florianopolis', 'FL', 580000)")
cursor.execute("insert into population values('Sao Paulo', 'SP', 6400000)")


conn.commit()

conn.close()