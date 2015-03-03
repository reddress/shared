SOURCE_DIR = "c:/Users/Heitor/Desktop/emacs-24.3/bin/tmp/AAAutomation2014data/"

DEST_DIR = "c:/Users/Heitor/Desktop/emacs-24.3/bin/tmp/AAAutomation2014data/cleaned/"

CLEAN_DATE = "26/02/2015"

import os
import glob

def clean_data(filename):
    os.chdir(SOURCE_DIR)
    with open(filename) as input_file:
        with open(DEST_DIR + filename, 'w') as output_file:
            lines = input_file.readlines();
            product_data = lines[0].split(";")
            qtde_por_caixa = product_data[-1].strip()
            
            print(CLEAN_DATE + ";0;0;0;0;" + qtde_por_caixa, file=output_file)
            print("".join(lines[1:]), file=output_file, end="")
            

os.chdir(SOURCE_DIR)

sources_filenames = glob.glob("*.txt")

for source_filename in sources_filenames:
    clean_data(source_filename)
