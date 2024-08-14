import sqlite3 as sq

with sq.connect("first.db") as con:
    cur = con.cursor()

cur.execute("""
""")



con.close()