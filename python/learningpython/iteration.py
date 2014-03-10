L = [1, 2, 3]
I = iter(L)
next(I)

[line.upper() for line in open('python/progress.txt')]
[(line.rstrip(), len(line.rstrip())) for line in open('python/progress.txt')]

cards = [rank + suit for rank in "23456789TJQKA" for suit in "CDHS"]
cards

matrix = [(x,y,z) for x in range(4) for y in range(4) for z in range(2)]
matrix

sorted(open('python/progress.txt'))
sorted(filter(lambda line: len(line) > 1, open('python/progress.txt')))

"|".join(filter(bool, map(str.rstrip, open('python/progress.txt'))))

# p. 432
# extend iterates the extension automatically
# example: lst.append(file_in) results in TextIOWrapper added
# lst.extend results in actual lines from file being added

# p. 441 quiz
# 1. for loop traverses elements of the iterable
# 2. list comp. is shorter and practically a backwards for loop
# 3. comprehensions, for loop, next, ?
# 4. for line in open("...")
# 5. holy hand grenade

