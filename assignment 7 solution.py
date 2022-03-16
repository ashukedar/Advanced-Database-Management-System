import mysql.connector

cnx = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="assign7")

cur = cnx.cursor()

#1
janSalary = float(input("Enter the Jan salary: "))
febSalary = float(input("Enter the Feb salary: "))
marSalary = float(input("Enter the Mar salary: "))
print("Total Salary for quarter 1:", janSalary + febSalary + marSalary)

#2
cur.execute("""
CREATE TABLE instructor(
    ID int,
    name varchar(200),
    dept_name varchar(200),
    salary numeric(10,2),
    age numeric(10,0)
);""")
instructors = [
    (10101,'Srinivasan','Comp. Sci.',65000, 34),
	(12121,'Wu','Finance',90000, 38),
	(15151,'Mozart','Music',40000, 45),
	(22222,'Einstein','Physics',95000, 55)]
cur.executemany("""
    INSERT INTO 
    instructor(ID, name, dept_name, salary, age)
    VALUES (%s, %s, %s, %s, %s)""", instructors)

#3
cur.execute("""
CREATE FUNCTION isEligible(age INTEGER) 
    RETURNS VARCHAR(20) 
    BEGIN 
        RETURN IF(age>40, 'YES', 'NO'); 
    END;""")

cnx.commit()
cnx.close()