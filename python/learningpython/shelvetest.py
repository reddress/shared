import shelve
import datetime

db = shelve.open('codshelf')
db['title'] = 'codigos'

db.close()


type(db['title'])
print("2")


print(2/2)



help(datetime)
now = datetime.datetime.now()
now
now.strftime("%Y_%m_%d")
import os
os.getcwd()
