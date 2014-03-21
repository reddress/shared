"""
How to store data?

dictionary d['ai4'] = "

tree?
ex. "yan3 chang4 hui4"
looks for all entries under yan3 -> ang4 -> ui4 -> [return a list]
while "tian3 wang4" would search yan3 -> ang4 -> [return a list]

root = {}
root['yan3'] = {}
root['yan3']['list'] = [102, 115, 3]  # ids of ['yan3', 'mian3', 'qian3', ...]
root['yan3']['ang4'] = {}
root['yan3']['ang4']['list'] = [192, 301, ...]  # ids of ['tian3 wang4', ...]

for a len-3 word, suggest 3-deep, 2-deep and 1-deep rhymes:
-an3 -ang4 -ui4
-ang4 -ui4
-ui4

make endings uniform
http://en.wikipedia.org/wiki/Pinyin_table
"""
