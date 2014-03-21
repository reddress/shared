# convert pinyin endings to more uniform representation

import init
init.init()

table = open("convtable.txt")
py2alt = {}
for line in table:
    endings = line.strip().split(",")
    py2alt[endings[0]] = endings[1]
table.close()

def convert(syl, savetone=True):
    base = syl[0:-1]
    if savetone:
        tone = syl[-1]
    else:
        tone = ""
    try:
        modifiedbase = py2alt[base]
    except KeyError:
        modifiedbase = base
    #return modifiedbase + tone
    #discard consonants
    vowels = set("aeiouwy")
    index = 0
    for char in modifiedbase:
        #print("char", char)
        if char in vowels:
            #print("found at index", index)
            return modifiedbase[index:] + tone
        index += 1
    return modifiedbase + tone

#convert("wan3")
#convert("quan2")

def extractendings(entry):
    py = entry[entry.find("[") + 1:entry.find("]")]
    return " ".join(map(lambda s: convert(s, True), py.split()))
    
#cedict = open("cedictsnippet.txt", encoding="utf-8")
#for line in cedict:
#    print(extractendings(line))
#cedict.close()
