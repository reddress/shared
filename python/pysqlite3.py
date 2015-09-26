#!/usr/bin/env python3

import sqlite3
import sys

dbfile = "/home/heitor/tmp/python/tmpdb.db"

def create(cur):
    try:
        cur.execute('''create table if not exists
        person (id int, name varchar(80),
        constraint pk_person primary key (id))''')
    except sqlite3.Error as e:
        print(e)

# Create
def insert(cur, id, name):
    try:
        cur.execute('''insert into person (id, name)
        values (?, ?)''', (id, name))
        print("tried inserting " + name)
    except sqlite3.Error as e:
        print("INSERT error for", name, e)
        
# Read
def selectId(cur, id):
    try:
        cur.execute('''select name from person where id = ?''', (id,))
        print(cur.fetchone())
    except sqlite3.Error as e:
        print("SELECT ID error:", id, e);      
        
# Update
def update(cur, id, newName):
    try:
        cur.execute('''update ''')

    except sqlite3.Error as e:
        print("UPDATE error:", e)
        
def main():
    conn = sqlite3.connect(dbfile)

    with conn:
        
        cur = conn.cursor()

        cur.execute("select sqlite_version()")
        data = cur.fetchone()

        print(data)

        create(cur)
        insert(cur, 1, "Tina")
        insert(cur, 2, "Ken")
        conn.commit()

        selectId(cur, 2)
        print("All done")

if __name__ == "__main__":
    main()
