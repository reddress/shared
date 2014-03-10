import shelve

db = shelve.open("python/persondb")
print(db["Sue Jones"])
tom = db["Tom Lane"]
db.close()
tom.shout()
