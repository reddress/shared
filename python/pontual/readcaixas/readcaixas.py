import os
import glob

os.chdir('c:\\Users\\Heitor\\Desktop\\emacs-24.3\\bin\\shared\\python\\pontual\\readcaixas\\data')

filenames = glob.glob('*.txt')

for filename in filenames:
    with open(filename) as f:
        firstline = f.readlines()[0].strip()
        print(filename.split(".")[0] + "," + firstline.split(";")[-1])
