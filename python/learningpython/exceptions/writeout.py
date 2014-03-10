import os
os.chdir("/home/heitor/python/learningpython/exceptions")
out = open("out.txt", "w")
try:
    print("start", file=out)
    print(1/0, file=out)
finally:
    print("got to finally")
