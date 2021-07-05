#1. Create a connection for DB and print the version using a python program

import mysql.connector

pskdb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1609"
)
print(pskdb)


import sys
cur = pskdb.cursor()
cur.execute("SELECT VERSION()")
data = cur.fetchone()
print("DBMS Version :",str(data))


#2. Create a multiple tables & insert data in table

dbse = pskdb.cursor()

dbse.execute("CREATE DATABASE pskdb")
dbse = pskdb.cursor()
dbse.execute("SHOW DATABASES")

for entry in dbse:
  print(entry)


pskdb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1609",
  database="pskdb"
)
dbse = pskdb.cursor()

dbse.execute("CREATE TABLE customers (Employee_name VARCHAR(255), Employee_dep VARCHAR(255), Employee_id VARCHAR(255))")

dbse = pskdb.cursor()

dbse.execute("SHOW TABLES")

for value in dbse:
  print(value)


dbse = pskdb.cursor()

dbse.execute("CREATE TABLE Office (emp_name VARCHAR(255), Employee_id VARCHAR(255) ,EMP_ADDRESS VARCHAR(255))")

dbse =pskdb.cursor()

dbse.execute("CREATE TABLE Student(rollno INT(24) , STUD_NAME VARCHAR(255) , MARK INT(3))")

dbse = pskdb.cursor()

dbse.execute("SHOW TABLES")

for value in dbse:
  print(value)

#3. Create a employee table and read all the employee name in the table using for loop
pskdb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1609",
  database="pskdb"
)

mycursor = pskdb.cursor()

mycursor.execute("CREATE TABLE Employee1 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

pskdb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1609",
  database="pskdb"
)
mycursor = pskdb.cursor()

sql = "INSERT INTO Employee1 (id, name, address) VALUES (%s, %s,%s)"
val = ("1600","Puneet Singh","362,phase-3")
mycursor.execute(sql, val)

pskdb.commit()

print(mycursor.rowcount, "record inserted.")

mycursor = pskdb.cursor()

sql = "INSERT INTO Employee1 (id, name, address) VALUES (%s, %s,%s)"
val = ("2804","Raman","Pratap nagar")
mycursor.execute(sql, val)

pskdb.commit()

print(mycursor.rowcount, "record inserted.")

mycursor = pskdb.cursor()

sql = "INSERT INTO Employee1 (id, name, address) VALUES (%s, %s,%s)"
val = ("2201","Manav","Phase - 1")
mycursor.execute(sql, val)

pskdb.commit()

print(mycursor.rowcount, "record inserted.")
mycursor = pskdb.cursor()

sql = "INSERT INTO Employee1 (id,name, address) VALUES (%s,%s,%s)"
val = [
  ('1','Psk', 'phase-2'),
  ('2','Amy', 'model town'),
  ('3','Honey','sarabja nagar'),
  ('4','Manpreet', 'silicon valley'),
  ('5','Sims', 'toronto'),
  ('6','Pankaj', 'Canada')
]

mycursor.executemany(sql, val)

pskdb.commit()

print(mycursor.rowcount, "was inserted.")
mycursor = pskdb.cursor()

mycursor.execute("SELECT * FROM Employee1")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mycursor = pskdb.cursor()

mycursor.execute("SELECT name FROM Employee1")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
