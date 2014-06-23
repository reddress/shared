# local file in c:/Python33/Lib/site-packages/
#
# after editing and testing, copy to
# /shared/python/sql/

import mysql.connector

cnx = None
cursor = None

def connect(db):
    global cursor
    global cnx
    #cnx = mysql.connector.connect(user='tina', password='tina3', host='127.0.0.1', database='learning')
    cnx = mysql.connector.connect(user='tina', password='tina3', host='127.0.0.1', database=db)
    cursor = cnx.cursor()

def run(sql):
    global cursor
    cursor.execute(sql)

def commit():
    global cnx
    cnx.commit()

def tbl():
    global cursor
    tbl_copy = list(cursor)[:]
    tbl_str = []
    
    # convert all to str
    for row in tbl_copy:
        tbl_str.append([str(entry) for entry in row])
    
    columns = len(tbl_str[0])
    col_max = [len(tbl_str[0][col]) for col in range(columns)]
    for row in tbl_str:
        for col_index in range(columns):
            if row[col_index] == None:
                col_max[col_index] = 4
            elif len(row[col_index]) > col_max[col_index]:
                col_max[col_index] = len(row[col_index])
    def get_padded_format_string(widths):
        return "| {:" + "}| {:".join([str(n+1) for n in widths]) + "}|"

    print()
    for row in tbl_str:
        print(get_padded_format_string(col_max).format(*row))

def close():
    global cnx, cursor
    cnx.close()
    cursor = None

def sel(sql):
    run(sql)
    tbl()
