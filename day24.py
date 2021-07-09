#import json
school = [
    {"name":"lucky","id":11,"section":"A"},
    {"name":"ram","id":12,"section":"A"},
    {"name":"sam","id":15,"section":"B"},

]
with open("school.json","w") as file:
    data= json.dump(school,file)
json_string = json.dumps(data)
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="8639488740",
    database="testdb"
)
curr = mydb.cursor()
curr.execute("CREATE TABLE tutee(name VARCHAR(30),id int , section CHAR(10))")
sql = "INSERT INTO tutee(name,id,section) VALUES (%s,%s,%s)"
values = json_string
curr.execute(sql,values)
mydb.commit()
curr.close(
