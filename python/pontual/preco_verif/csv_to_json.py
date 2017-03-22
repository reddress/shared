import csv
import json

# TAB_FILE = "d:/pontual/produtos/precos_few.csv"
# JSON_FILE = "d:/pontual/produtos/precos_few.json"

TAB_FILE = "d:/pontual/produtos/precos_desc_2017_03_17_b.csv"
JSON_FILE = "d:/pontual/produtos/precos_html/precos_desc_2017_03_17.json"

def process():
    csv_file = open(TAB_FILE)
    json_file = open(JSON_FILE, 'w')

    field_names = ("COD","NOME","TAB","-6%","-7%","-8%")

    reader = csv.DictReader(csv_file, field_names)

    print('var precos={', end="", file=json_file)

    for row in reader:
        # Exclude codigos with 2 letters (8 chars) because price may
        # be lower
        if len(row['COD']) < 8:
            print('"{}":'.format(row['COD'][:6]), end="", file=json_file)
            json.dump(row, json_file)
            print(',', file=json_file)

    print('"END":{}};', file=json_file)  # to avoid trailing comma
