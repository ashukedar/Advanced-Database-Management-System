import mysql.connector

cnx = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="assign4")

cur = cnx.cursor()

cnx.commit()
cnx.close()