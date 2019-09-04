import csv
from pprint import pprint
import json

data = open("data2.csv")
reader = csv.DictReader(data)

def output_json():
    content = json.dumps([row for row in reader], indent=4)
    # normal_list = [row for row in reader]
    with open('data2.json', 'w') as file:
        file.write(content)

def output_xml():
    xml = ['<?xml version="1.0" encoding="UTF-8"?>'] #first line of the file
    for row in reader:
        xml.append('<bank>')
        for k, v in row.items():
            xml.append(f'    <{k}>{v}</{k}>')
        xml.append('</bank>')
    with open('data2.xml', 'w') as file:
        file.write('\n'.join(xml))

def total_deposits():
    total = 0
    for row in reader:
        total += int(row['DEPSUM'].replace(',',''))

    print(f'total: ${total}')

def bank_deposits():
    deposits = {}
    for row in reader:
        if row['NAMEFULL'] not in deposits:
            deposits[row['NAMEFULL']] = 0
        deposits[row['NAMEFULL']] += int(row['DEPSUM'].replace(',',''))

    deplist = []
#create list of dicts to be able to sort te data easy
    for k, v in deposits.items():
        deplist.append({
            'name': k,
            'deposits': v
        })
    deplist.sort(key= lambda k: k['deposits'])
    pprint(deplist)

print('[1] convert to json')
print('[2] convert to xml')
print('[3] show total deposits')
print('[4] show deposits by bank')
print('')
choice = int(input('what would you like to do? '))

if choice == 1:
    output_json()
if choice == 2:
    output_xml()
if choice == 3:
    total_deposits()
if choice == 4:
    bank_deposits()