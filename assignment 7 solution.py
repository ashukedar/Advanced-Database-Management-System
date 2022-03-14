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

cnx.commit()
cnx.close()