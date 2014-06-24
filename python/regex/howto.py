# https://docs.python.org/3.4/howto/regex.html

import re
p = re.compile("cad*")
m = p.search("abracadabra")  # p.match() only matches beginning of string
m.group()
m.start(), m.end()

