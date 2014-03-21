# build Python dictionaries mapping endings to list of matching words
# full data dict. has trad. as key

from convertpy import extractendings

def gettrad(entry):
    return entry.split()[0]
    
cedict = open("cedictsubset.txt", encoding="utf-8")
words = {}    # key is traditional characters
matches = {}  # key is word endings

for line in cedict:
    trad = gettrad(line)
    endings = extractendings(line)
    words[trad] = line.strip()
    if endings in matches:
        matches[endings] += " " + trad
    else:
        matches[endings] = trad

def match(endings):
    for match in matches[endings].split():
        print(words[match])

def matchfromentry(entry):
    match(extractendings(entry))

def matchfromword(word):
    match(extractendings(words[word]))
    # for simplified, use try block, first attempting trad, then
    # simp -> trad, if still not found return not found
    # create translation table from simp to trad
