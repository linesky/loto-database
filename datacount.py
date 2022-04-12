import sqlite3
con=sqlite3.connect("my.db")
list1=range(1,50)
for nn in list1:
	cur=con.execute("SELECT COUNT (nmb) as n FROM numbers WHERE nmb="+str(nn))
	t=-1
	for n in cur:
		t=t+1
		if t==0:
			print str(nn)+"\t"+str(n[0])
		else:
			cur.close()
			
con.close()
