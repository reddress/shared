# convert pinyin endings to more uniform representation

import init
init.init()

table = open("convtable.txt")
py2alt = {}
for line in table:
    endings = line.strip().split(",")
    py2alt[endings[0]] = endings[1]
table.close()
