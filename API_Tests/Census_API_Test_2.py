import requests
import json
# import csv

all_data = []

#
# r = requests.get('https://api.census.gov/data/2014/pep/natstprc?get=STNAME,POP&DATE_=7&for=state:*')
# print(r.status_code)

# 7 after date (predicate) is July

# we get pep/natstprc as acronym from Census Data API Dataset page: https://api.census.gov/data.html
# https://api.census.gov/data/2014/pep/natstprc is base URL for Dataset
# Variabels link on that page lets you know what you can query

# data = json.loads(r.text)
# print(data)



# payload = {'q': 'STNAME', 'q': 'POP'}
# r = requests.get('https://api.census.gov/data/2014/pep/natstprc&DATE_=7&for=state:*', params=payload)
# print(r.status_code)
#
# data = json.loads(r.text)
# print(data)


r = requests.get('https://api.census.gov/data/2010/surname?get=NAME,COUNT&RANK=1:100')
print(r.status_code)

data = json.loads(r.text)
for row in data:
    print(row[2],row[0],row[1])

# for row in data:
#
#     name_listing={'rank': row[2],'name': row[0], 'count': row[1]}
#     all_data.append(name_listing)
#
# json.dump(all_data, open('census_surname_test.json', 'w'), indent=2)
#
# with open('census_surname_test.json', 'r') as working_file:
#     print([0])

# print(data)
