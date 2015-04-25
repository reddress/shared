import urllib.request
from urllib.request import FancyURLopener as fancy

opener = fancy()
opener.version="Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:27.0) Gecko/20121011 Firefox/27.0"

def dl(urlroot, start, end, zeros, tail, dest):
    for i in range(end - start + 1):
        num = str(start + i).zfill(zeros)
        print(urlroot + num + tail)
        try:
            opener.retrieve(urlroot + num + tail, dest + "_" + num + tail)
        except ValueError:
            print("ERROR with " + num)

def dlskip(urlroot, start, end, skip, zeros, tail, dest):
    for i in range(0, end - start + 1, skip):
        num = str(start + i).zfill(zeros)
        print(urlroot + num + tail)
        opener.retrieve(urlroot + num + tail, dest + "_" + num + tail)

def dllist(urlroot, indices, zeros, tail, dest):
    for index in indices:
        num = str(index).zfill(zeros)
        print(urlroot + num + tail)
        opener.retrieve(urlroot + num + tail, dest + "_" + num + tail)
