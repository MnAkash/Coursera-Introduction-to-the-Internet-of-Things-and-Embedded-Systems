# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 02:59:14 2020

@author: akash
"""

import urllib.request, urllib.parse, urllib.error
import json


count = 0
sum = 0
link = input('Enter location: ')#http://py4e-data.dr-chuck.net/comments_486881.json
print('Retrieving', link)
html = urllib.request.urlopen(link).read().decode()
print('Retrieved', len(html), 'characters')

try:
    data = json.loads(html)
except:
    raise Exception("Couldn't retreive Data")


for item in data['comments']:
    count += 1
    sum += int(item['count'])

print('Count:', count)
print('Sum:', sum)