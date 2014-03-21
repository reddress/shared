# remove any entry that is longer than 3 characters or that includes
# any character outside the Taiwan school list

from compiletaiwanlist import taiwanchars
import init
init.init()
out = open("cedictsubset.txt", "w", encoding="utf-8")
cedict = open("cedict_ts.txt", encoding="utf-8")
for line in cedict:
    trad = line.split()[0]
    firstpychar = line[line.find("[") + 1]
    if (len(trad) < 4 and set(trad).issubset(taiwanchars) and
        firstpychar.islower()):
        print(line, end="", file=out)
out.close()
cedict.close()
