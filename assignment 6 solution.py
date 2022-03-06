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

#5
cur.execute("""CREATE USER 'ashutosh'@'localhost' IDENTIFIED BY 'password';
GRANT student to 'ashutosh'@'localhost';""")

#6
#cur.execute("GRANT SELECT ON faculty To 'ashutosh'@'localhost';")
cur.execute("REVOKE SELECT ON faculty FROM 'ashutosh'@'localhost';")

#7
cur.execute("DROP role student")

cnx.commit()
cnx.close()