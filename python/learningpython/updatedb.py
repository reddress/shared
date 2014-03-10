import shelve

db = shelve.open("python/persondb")

for key in sorted(db):
    print(key, ":", db[key])
db['Sue Jones'].giveRaise(10) # doesn't work
sue = db['Sue Jones']
sue.giveRaise(10)
db['Sue Jones'] = sue
db.close()
