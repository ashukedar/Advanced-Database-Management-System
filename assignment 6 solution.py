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

cnx.commit()
cnx.close()