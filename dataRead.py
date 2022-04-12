import sqlite3
con=sqlite3.connect("my.db")
cur=con.execute("SELECT * FROM numbers")
for n in cur:
		print n
con.close()
