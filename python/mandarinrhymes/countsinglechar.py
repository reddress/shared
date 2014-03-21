# count unique characters in CEDICT entries

import init
init.init()
cedict = open("cedict_ts.txt", encoding="utf-8")
charset = set()
for line in cedict:
    trad = line.split()[0]
    for char in trad:
        charset.add(char)
charlist = list(charset)
cedict.close()
