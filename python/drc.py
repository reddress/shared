# dr chrono

import sys

def match_same_length(s, pat):
    print(s)
    for i in range(len(pat)):
        if pat[i] == "*":
            continue
        elif pat[i] == s[i]:
            continue
        else:
            return 0
    return 1

def count_matches(s, pat):
    cursor = 0
    count = 0
    while cursor < len(s) - len(pat) + 1:
        if match_same_length(s[cursor:cursor+len(pat)], pat):
            count += 1
            cursor += 1
        else:
            cursor += 1
    return count

lines = sys.stdin.readlines()
print(count_matches(lines[1].strip(), lines[2].strip()))

count_matches("ABCDDDDABCDABCDDCCCB", "AB*D")

###

name_file = """MERVIN:865965036
BOUCK,MERVIN:865965036
MERVIN BOUCK:865965036
BOUCK,MERVIN ADELINE:865965036
MERVIN ADELINE BOUCK:865965036
LEN:992989227
GERALD:358648156
BYER,GERALD:358648156
GERALD BYER:358648156"""

name_file = """HOLLIS LEANDRA MILLS:715861502
GARD,DREW:165871010
ELDA:994159653
FRITSCHE,SO RAUL:083148476
FERREE,THRESA:229225483
THRESA FERREE:229225483"""

name_file

import sys
lines = sys.stdin.readlines()[1:]

lines = name_file.split("\n")

def compare(name, existing_name):
    # reverse if comma is there
    if "," in name:
        name_parts = name.split(",")
        name = name_parts[1] + " " + name_parts[0]
    if existing_name == "":
        return name

    no_comma_name_parts = name.split()
    existing_name_parts = existing_name.split()

    if len(no_comma_name_parts) > len(existing_name_parts):
        return name
    
    new_parts = []
    for i in range(len(no_comma_name_parts) - 1):
        if len(no_comma_name_parts[i]) > len(existing_name_parts[i]):
            new_parts.append(no_comma_name_parts[i])
        else:
            new_parts.append(existing_name_parts[i])
    new_parts.append(no_comma_name_parts[-1])
    name = " ".join(new_parts)
    
    return name

directory = {}
out = ""
order = []
for line in lines:
    name, ssn = line.strip().split(":")
    if not ssn in directory:
        order.append(ssn)
    if ssn in directory:
        current_name = directory[ssn]
    else:
        current_name = ""
    directory[ssn] = compare(name, current_name)
for ssn in order:
    out += "%s:%s\n" % (directory[ssn], ssn)
print(out)
