import sqlite3
con = sqlite3.connect("my_test_db1")

print("Enter roll number, which you want to delete")

r1 = input()
query = "delete from stud_info where sroll=" + r1

con.execute(query)
con.commit()
con.close()
print("Data deleted...")
