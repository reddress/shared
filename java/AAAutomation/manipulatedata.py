# update first line to reflect new fields

import glob
import os
import codecs

DATA_DIR = "c:/Users/Heitor/Desktop/emacs-24.3/bin/shared/java/AAAutomation/data/"

os.chdir(DATA_DIR)

data_glob = glob.glob("*.txt")

for filename in data_glob:
    with open(DATA_DIR + filename, encoding="utf8") as f:
        first_line = f.readline()
        rest = f.readlines()
        fields = first_line.split(";")
        if len(fields) < 5: 
            fields.insert(1, '0')
            fields.insert(2, '0')
            fields.insert(4, '0')

    out = codecs.open(DATA_DIR + filename, 'w', encoding="utf8")
    out.write(";".join(fields))
    out.write("".join(rest))
    out.close()
