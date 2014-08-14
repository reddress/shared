import os
import glob

DATA_DIR = "c:/Users/Heitor/Desktop/emacs-24.3/bin/shared/java/AAAutomation/data/"

OUTPUT = DATA_DIR + "qtdecaixa.csv"

os.chdir(DATA_DIR)

data_files = glob.glob("*.txt")

outfile = open(OUTPUT, 'w')

for filename in data_files:
    with open(filename) as file:
        line = file.readline().strip()
        values = line.split(";")
        print(filename[:-4] + ";" + values[-1], file=outfile)

outfile.close()
