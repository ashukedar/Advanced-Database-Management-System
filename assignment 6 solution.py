import mysql.connector

cnx = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="assign4")

cur = cnx.cursor()

#1
cur.execute("""CREATE VIEW Faculty AS
SELECT ID, Dept_name, Name
FROM instructor;""")

#2
cur.execute("""CREATE VIEW View2 AS
SELECT Dept_name, SUM(Salary)
FROM instructor
GROUP BY Dept_name;""")

#3
cur.execute("CREATE ROLE student;")

#4
cur.execute("""GRANT SELECT on faculty
TO student;""")

cnx.commit()
cnx.close()