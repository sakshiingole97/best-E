#1. Create an Employee Table with employee name,employee ID & Salary
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1609",
)

mycursor = mydb.cursor()
print(mydb)


dbse = mydb.cursor()

dbse.execute("CREATE DATABASE Employee_Mangement")
dbse = mydb.cursor()

dbse.execute("SHOW DATABASES")

for entry in dbse:
    print(entry)


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1609",
    database="employee_mangement"
)
dbse = mydb.cursor()

dbse.execute("CREATE TABLE Employee (emp_id INT , EMP_NAME VARCHAR(255),EMP_SALARY DOUBLE )")


dbse = mydb.cursor()

dbse.execute("SHOW TABLES")

for value in dbse:
  print(value)


dbse = mydb.cursor()

dbse.execute("SHOW COLUMNS FROM employee")

for value in dbse:
  print(value)

dbse = mydb.cursor()

sql = "INSERT INTO employee (emp_id , EMP_NAME , EMP_SALARY) VALUES (%s,%s,%s)"
val = [
    ('101','Puneet','1500.0'),
    ('102','manav','100.0'),
    ('103','shiv','7846.0'),
    ('104','Kanav','9856.0'),
    ('105','Puneetpsk','885.0'),
    ('106','Anchal','7432.0'),
    ('107','kawal','1234.0'),
    ('108','Abhi','12345.0'),
    ('109','Manvir','6598.0'),
    ('110','Taran','73691.0'),
    ('111','Daman','9137.0'),
    ('112','Gurleen','1012.0'),
    ('113','Aditi','102375.0'),
    ('114','PuneetSingh','8567.0'),
    ('115','Karanjot','80502.0')
       
]

dbse.executemany(sql, val)

mydb.commit()

print(dbse.rowcount, "records were inserted.")
#a. Write a query to get the maximum and minimum salary from employees table
mycursor = mydb.cursor()

mycursor.execute("SELECT EMP_NAME,EMP_SALARY FROM employee where EMP_SALARY = (select max(EMP_SALARY) from employee)")

myresult = mycursor.fetchall()

for i in myresult:
    print(i)

mycursor = mydb.cursor()

mycursor.execute("SELECT EMP_NAME,EMP_SALARY FROM employee where EMP_SALARY = (select min(EMP_SALARY) from employee)")

myresult = mycursor.fetchall()

for i in myresult:
    print(i)

# b. Write a query to get the number of employees working with the company
mycursor = mydb.cursor()

mycursor.execute("SELECT COUNT(*) from employee")

myresult = mycursor.fetchall()

for i in myresult:
    print(i)

#c. Write a query to get the first 3 characters of first name from employees table

mycursor = mydb.cursor()

mycursor.execute("SELECT * from employee WHERE EMP_NAME LIKE('ANU%')")

myresult = mycursor.fetchall()

for i in myresult:
    print(i)
