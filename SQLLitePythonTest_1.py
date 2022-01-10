import sqlite3
con = sqlite3.connect("my_test_db1")

print("Enter Student Roll number")
r = input()

print("Enter Student name")
nm=input()

print("Enter Student city")
ct = input()


query = "insert into stud_info(sroll,sname,scity) values(" +r + ",'" + nm + "','" +ct +"')"
con.execute(query)
con.commit()
con.close()
print("Data saved...")

