# set back dates matching 28/07 and in produtodb

import os
import os.path
import shelve
import codecs
import glob

from datetime import datetime

DATA_DIR = "c:/Users/Heitor/Desktop/emacs-24.3/bin/shared/java/AAAutomation/data/"

def read_caixa(f):
    with open(DATA_DIR + f, encoding="utf8") as infile:
        firstline = infile.readline().strip()
        firstline_parts = firstline.split(";")
        if firstline_parts[2].strip() == "0":
            #print(f + "|" + firstline_parts[2] + "|")
            print(f[:-4])

os.chdir(DATA_DIR)
for f in glob.glob("*.txt"):
    read_caixa(f)
