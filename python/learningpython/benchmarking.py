import timeit

timeit.repeat(stmt="[x ** 2 for x in range(1000)]", number=1000, repeat=5)

# p. 662 quiz
# 1. map, list comp are fastest
# 2. pypy fastest, py 3 slowest

