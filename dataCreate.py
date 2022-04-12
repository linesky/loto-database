import random
import sqlite3
con=sqlite3.connect("my.db")
cur=con.execute("CREATE TABLE numbers(idx INTEGER,nmb INTEGER)")
list1=range(0,50)
random.SystemRandom(random.random())
for n in list1:
	cur.execute("INSERT INTO numbers VALUES("+str(n)+","+str(random.randrange(1,50))+")")
	
con.commit()
con.close()
