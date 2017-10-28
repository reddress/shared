from html.parser import HTMLParser
from collections import Counter
import random

# http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/

# HTML_FILE = "/home/heitor/tmp/D_MEGA_short.HTM"
HTML_FILE = "/home/heitor/tmp/D_MEGA.HTM"

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.td_count = 0
        self.jogo = 0
        
    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self.td_count = 0
            
        elif tag == "td":
            self.td_count += 1

    def handle_data(self, data):
        try:
            num_jogo = int(data)
            if self.td_count == 1 and 1 <= num_jogo <= 9999:
                print("\nJogo {}".format(num_jogo), end=" ")

            if 3 <= self.td_count <= 8 and data.strip() != "":
                print(" {}".format(data), end="")
                sorteados.append(int(data))
        except:
            pass

def parseHTML():
    sorteados = []

    myfile = open(HTML_FILE, encoding="iso-8859-1")
    data = myfile.read()
    myfile.close()
    
    p = MyHTMLParser()
    p.feed(data)
    print()

    c = Counter(sorteados)
    return c

# as of Jogo 1981
# [(k, c[k]) for k in sorted(c, key=c.get, reverse=True)]

c_sorted = [(5, 228), (53, 226), (10, 221), (4, 218), (23, 218), (51, 218), (33, 216), (54, 215), (17, 214), (24, 214), (42, 212), (52, 212), (28, 211), (30, 210), (16, 209), (43, 209), (13, 208), (32, 208), (41, 208), (2, 205), (29, 203), (50, 203), (27, 202), (34, 202), (37, 201), (44, 201), (36, 200), (6, 199), (47, 199), (49, 199), (56, 199), (8, 198), (12, 198), (18, 198), (45, 198), (1, 197), (59, 196), (38, 194), (35, 193), (31, 192), (3, 190), (20, 189), (58, 189), (11, 188), (7, 187), (60, 186), (40, 185), (48, 185), (57, 185), (19, 184), (46, 184), (39, 183), (9, 181), (15, 181), (25, 181), (14, 180), (21, 173), (22, 171), (55, 170), (26, 162)]

def simJogo():
    dezenas = list(range(1, 61))
    random.shuffle(dezenas)
    return dezenas[:6]

def simHistorico(jogos):
    sorteados = []
    for i in range(jogos):
        sorteados.extend(simJogo())
    c = Counter(sorteados)
    return c

def test():
    pass
