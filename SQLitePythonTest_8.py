import sqlite3
con = sqlite3.connect("my_test_db1")
query = "select * from stud_info"
cur = con.cursor()
cur.execute(query)
while True:
    data = cur.fetchone()
    if data != None:
        print(data)
    else:
        break

cur.close()
con.close()