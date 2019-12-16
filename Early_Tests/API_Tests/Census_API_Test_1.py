import requests
import json
# import csv
#
r = requests.get('https://api.census.gov/data/2014/pep/natstprc?get=STNAME,POP&DATE_=7&for=state:*')
print(r.status_code)

# 7 after date (predicate) is July

# we get pep/natstprc as acronym from Census Data API Dataset page: https://api.census.gov/data.html
# https://api.census.gov/data/2014/pep/natstprc is base URL for Dataset
# Variables link on that page lets you know what you can query

data = json.loads(r.text)
print(data)


# something doesn't work here
# payload = {'q': 'STNAME', 'q': 'POP'}
# r = requests.get('https://api.census.gov/data/2014/pep/natstprc&DATE_=7&for=state:*', params=payload)
# print(r.status_code)
#
# data = json.loads(r.text)
# print(data)
