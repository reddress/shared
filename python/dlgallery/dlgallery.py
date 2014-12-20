import urllib.request
from urllib.request import FancyURLopener as fancy

opener = fancy(version="Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11")

def dl(urlroot, start, end, zeros, tail, dest):
    for i in range(end - start + 1):
        num = str(start + i).zfill(zeros)
        print(urlroot + num + tail)
        opener.retrieve(urlroot + num + tail, dest + "_" + num + tail)

