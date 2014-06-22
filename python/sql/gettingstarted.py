# open cmd
# cd \apache24
# httpd.exe

import mysql.connector
cnx = mysql.connector.connect(user='tina', password='tina3', host='127.0.0.1', database='mydb')
cursor = cnx.cursor()

cursor.execute("SELECT * FROM corp;")  # result is an iterable
list(cursor)

cursor.execute("INSERT INTO corp (corp_id, name) VALUES (12, 'Incorp');")
cnx.commit()
