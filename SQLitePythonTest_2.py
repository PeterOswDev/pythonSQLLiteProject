import sqlite3

con = sqlite3.connect("my_test_db1")

print("Enter Student roll number, which you want to update")
r1 = input()

print("Enter student name, which you want to update")
nm = input()

print("Enter new city name, which you want to update")
ct =input()



query = "update stud_info set scity='" + ct + "',sname='" + nm + "' where sroll=" +r1

con.execute(query)
con.commit()
con.close()
print("Data Updated..")

