from sqlsetup import cursor

cursor.execute("""CREATE TABLE farmerhat
(hat_id SMALLINT,
type VARCHAR(30) CHARACTER SET big5,
CONSTRAINT pk_farmerhat PRIMARY KEY (hat_id));""")

cursor.execute("CREATE DATABASE learning")
