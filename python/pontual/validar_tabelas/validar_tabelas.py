import xlrd
from html.parser import HTMLParser

# Save Lista geral - ativos as listageral.xls

# Movimento > Lista de precos > Lista disponivel
# SALVAR EM C:/.../emacs-24.3/bin/validar_tabelas/listas_para_validar/

DIR_PREFIX = 'c:/Users/Heitor/Desktop/emacs-24.3/bin/validar_tabelas/listas_para_validar/'

def test():
    print("Run validar(filename...)")

def read_geral(filename_geral):
    cv_geral = {}
    timestamp = ""
    try:
        book = xlrd.open_workbook(filename_geral)
        sh = book.sheet_by_index(0)

        timestamp = sh.cell_value(rowx=1, colx=12)

        nrows = sh.nrows
        for row in range(nrows):
            cod_cell = sh.cell_value(rowx=row, colx=0)
            
            if isinstance(cod_cell, float):
                cod = str(int(cod_cell))
            
            elif isinstance(cod_cell, str):
                cod_cell = cod_cell.strip()
                if cod_cell == "" or cod_cell[0] == "C":
                    continue

                cod = cod_cell
            else:
                print(cod_type, "not recognized")

            try:
                cv_cell = sh.cell_value(rowx=row, colx=8)
            except ValueError:
                print("Error getting from lista geral cv cell on row", row)
                cv_cell = -1

            cv_geral[cod] = "%.2f" % cv_cell
    except FileNotFoundError as err:
        print(err)
        print("Could not load all files.")
    return timestamp, cv_geral

def read_xls(filename):
    cv_xls = {}
    disp_xls = {}
    resv_xls = {}

    timestamp = ""

    # cod cv disp resv
    # 0,  8,   9,  10

    try:
        book = xlrd.open_workbook(filename)
        sh = book.sheet_by_index(0)

        timestamp = sh.cell_value(rowx=1, colx=10)
        
        nrows = sh.nrows
        for row in range(nrows):
            cod_cell = sh.cell_value(rowx=row, colx=0)
            
            if isinstance(cod_cell, float):
                cod = str(int(cod_cell))
            
            elif isinstance(cod_cell, str):
                cod_cell = cod_cell.strip()
                if cod_cell == "" or cod_cell[0] == "C":
                    continue

                cod = cod_cell
            else:
                print(cod_type, "not recognized")

            try:
                cv_cell = sh.cell_value(rowx=row, colx=8)
            except ValueError:
                print("Error getting from XLS cv cell on row", row)
                cv_cell = -1

            try:
                disp_cell = int(sh.cell_value(rowx=row, colx=9))
            except ValueError:
                print("Error getting disponivel in xls row", row)
                disp_cell = -1000000

            try:
                resv_cell = int(sh.cell_value(rowx=row, colx=10))
            except ValueError:
                print("Error getting reserva cell in xls row", row)
                resv_cell = -1000000
            cv_left = "%.2f" % (int(cv_cell.split("/")[0].strip()) / 100)
            cv_xls[cod] = cv_left
            disp_xls[cod] = disp_cell
            resv_xls[cod] = resv_cell
                
    except FileNotFoundError as err:
        print(err)
        print("Could not load all files.")
    return (timestamp, cv_xls, disp_xls, resv_xls)

def find_cod(html_row):
    trial = html_row[0].strip()
    if len(trial) < 5 or trial[0] == 'C' or trial[0] == 'L':
        return None
    else:
        return trial
    
def add_dot(s):
    return s[:-2] + "." + s[-2:]

def find_cv(html_row):
    for td in reversed(html_row):
        if td.find("/") > -1:
            return add_dot(td.split("/")[0])

            
def read_html(filename):
    cv_html = {}
    disp_html = {}
    resv_html = {}

    html_rows = []
    
    class MyHTMLParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.td_idx = 0
            self.cur_row = []
            self.in_td = False
            self.row_ct = 0
            self.timestamp = ""
            
        def handle_starttag(self, tag, attrs):
            if tag == "tr":
                self.td_idx = 0
                html_rows.append(self.cur_row)
                self.cur_row = []
                self.row_ct += 1
                self.in_td = False
            elif tag == "font":
                self.td_idx += 1
                self.in_td = True
            else:
                self.in_td = False

        def handle_data(self, data):
            if self.in_td:
                if data.strip():
                    self.cur_row.append(data.strip().replace("\xa0", "").replace(".", ""))
            # get timestamp
            if self.row_ct == 3:
                try:
                    self.timestamp = self.cur_row[-1]
                except IndexError:
                    pass
            
    parser = MyHTMLParser()
    html_file = open(filename)
    html_str = html_file.read()
    html_file.close()
    
    parser.feed(html_str)
    for r in html_rows:
        if len(r) > 1:
            # print(r)
            cod = find_cod(r)
            if cod:
                cv = find_cv(r)
                cv_html[cod] = cv
                try:
                    disp_html[cod] = int(r[-2])
                    resv_html[cod] = int(r[-1])
                except ValueError:
                    disp_html[cod] = 0
                    resv_html[cod] = 0

    
    return (parser.timestamp, cv_html, disp_html, resv_html)
    
def validar(filename):
    filename_geral = DIR_PREFIX + "listageral.xls"
    filename_xls = DIR_PREFIX + filename + ".xls"
    filename_html = DIR_PREFIX + filename + ".HTM"
    
    timestamp_geral, cv_geral = read_geral(filename_geral)
    timestamp_xls, cv_xls, disp_xls, resv_xls = read_xls(filename_xls)
    timestamp_html, cv_html, disp_html, resv_html = read_html(filename_html)

    print()
    print()

    print("Lista Geral Timestamp:", timestamp_geral)
    print()
    
    print("XLS Timestamp:", timestamp_xls)
    print("HTML Timestamp:", timestamp_html)

    print()
    
    print("CV Geral len:", len(cv_geral))
    print("CV XLS len:", len(cv_xls))
    print("CV HTML len:", len(cv_html))

    print()

    print("Disp XLS/HTML len:", len(disp_xls), len(disp_html))
    print("Resv XLS/HTML len:", len(resv_xls), len(resv_html))

    print()
    print()
    
    if cv_geral != cv_xls:
        for k in cv_geral:
            try:
                if cv_geral[k] != cv_xls[k]:
                    print("CV Geral/XLS differ:", k)
            except KeyError:
                print("ERR: CV > XLS Key Error:", k)

        for k in cv_xls:
            try:
                if cv_geral[k] != cv_xls[k]:
                    print("CV Geral/XLS differ:", k)
            except KeyError:
                print("ERR: XLS > CV Key Error:", k)
                
    if cv_geral != cv_html:
        for k in cv_geral:
            try:
                if cv_geral[k] != cv_html[k]:
                    print("ERR: CV Geral/HTML differ:", k, cv_geral[k], cv_html[k])
            except KeyError:
                print("ERR: CV > HTML Key Error:", k)

        for k in cv_html:
            try:
                if cv_geral[k] != cv_html[k]:
                    print("ERR: CV Geral/HTML differ:", k, cv_geral[k], cv_html[k])
            except KeyError:
                print("ERR: HTML > CV Key Error:", k)

    if disp_xls != disp_html:
        for k in disp_xls:
            try:
                if disp_xls[k] != disp_html[k]:
                    print("ERR: Disp XLS/HTML differ:", k, disp_xls[k], disp_html[k])
            except KeyError:
                print("ERR: XLS > HTML disp Key Error:", k)

    if resv_xls != resv_html:
        for k in resv_xls:
            try:
                if resv_xls[k] != resv_html[k]:
                    print("ERR: Resv XLS/HTML differ:", k, resv_xls[k], resv_html[k])
            except KeyError:
                print("ERR: XLS > HTML resv Key Error:", k)


# display for autocomplete
print("\nRun validar(filename...)")
