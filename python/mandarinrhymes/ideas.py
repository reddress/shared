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

need to accept trad. chars, simp., and pinyin like zao3

store raw data as id -> entry

store ending sequences -> raw ids
ex. "an1 ao3 ei4" -> "203 102 401"


Python anywhere: run this in bash console
pip3.3 install --user https://github.com/davispuh/MySQL-for-Python-3/archive/1.0.
tar.gz

then in django settings
'ENGINE': 'mysql.connector.django',
'NAME': 'mandarinpandarin$django'
"""

# testing area
from convertpy import convert
convert("ju3")
convert("niu2")

def extractpy(entry):
    py = entry[entry.find("[") + 1:entry.find("]")]
    return " ".join(map(convert, py.split()))
cedict = open("cedictsnippet.txt", encoding="utf-8")
for line in cedict:
    print(extractpy(line))
