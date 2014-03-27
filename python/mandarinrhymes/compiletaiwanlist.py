# read Taiwan school list and produce a set of its characters

import init
init.init()
taiwanlist = open("taiwanschoollist.txt", encoding="utf-8")
taiwanchars = set()
for line in taiwanlist:
    for char in line:
        if char != " " and char != "\n":
            taiwanchars.add(char)
taiwanlist.close()
