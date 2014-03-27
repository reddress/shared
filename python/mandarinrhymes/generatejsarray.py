# create JavaScript array holding raw data

import init
init.init()
cedict = open("cedictsubset.txt", encoding="utf-8")
#cedict = open("cedictsnippet.txt", encoding="utf-8")
js = open("rawdata.html", "w", encoding="utf-8")
print("<script>cedict=[];", file=js)
for line in cedict:
    print("cedict.push('%s');" % line.strip().replace("'", r"\'"), file=js)
print("</script>", file=js)
cedict.close()
js.close()
