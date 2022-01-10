import sqlite3
con = sqlite3.connect("my_test_db1")
query = "select * from stud_info"
cur = con.cursor()
cur.execute(query)
data = cur.fetchmany(1)
print(data)


cur.close()
con.close()
