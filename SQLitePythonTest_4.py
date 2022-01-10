import sqlite3
con = sqlite3.connect("my_test_db1")
print("Enter city name, whose records you want to delete")
ct =input()
query = "delete from stud_info where scity='" + ct + "'"
con.execute(query)
con.commit()
con.close()
print("Data deleted...")