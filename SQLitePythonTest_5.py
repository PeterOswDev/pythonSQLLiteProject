import sqlite3

con = sqlite3.connect("my_test_db1")

cur = con.cursor()
query = "select sname, scity from stud_info where sroll >17"
cur.execute(query)
data = cur.fetchall()

print("type of data is: ",type(data))
print("\n")

for d in data:
    print("Roll number is: ", d[0])
    print("Name  is: ", d[1])


print(data)

cur.close()
con.close()