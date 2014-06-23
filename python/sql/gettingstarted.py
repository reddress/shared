# mysql starts automatically
#
# open cmd
# cd \apache24
# httpd.exe

# import mysql.connector
# cnx = mysql.connector.connect(user='tina', password='tina3', host='127.0.0.1', database='mydb')
# cursor = cnx.cursor()

# cursor.execute("""CREATE TABLE customer
# (cust_id SMALLINT,
# name VARCHAR(60) CHARACTER SET utf8,
# CONSTRAINT pk_customer PRIMARY KEY (cust_id));""")

# cursor.execute("SELECT * FROM corp;")  # result is an iterable
# list(cursor)

# cursor.execute("INSERT INTO corp (corp_id, name) VALUES (12, 'Incorp');")
# cnx.commit()

from sqlsetup import connect, run, commit, tbl, close

connect('learning')

run("SELECT * FROM person")
tbl()

run("DESC person")
tbl()

close()
