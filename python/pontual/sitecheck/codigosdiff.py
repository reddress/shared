import os
import glob

celia_codigos = set()

livesite_filename = "c:/users/heitor/Desktop/emacs-24.3/bin/shared/python/pontual/sitecheck/liveactivecodigos.txt"

with open(livesite_filename) as live_file:
    live_lines = live_file.readlines()

livesite_codigos = set([c.strip() for c in live_lines])

celia_folder = "C:/users/heitor/desktop/celia_categorias"

os.chdir(celia_folder)
for folder in glob.glob('*'):
    os.chdir(folder)
    for file in glob.glob('*'):
        celia_codigos.add(file[:-4])
    os.chdir("..")
