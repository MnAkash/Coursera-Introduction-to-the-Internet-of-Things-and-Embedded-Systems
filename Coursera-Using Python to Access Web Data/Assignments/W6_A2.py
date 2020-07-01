# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 03:08:51 2020

@author: akash
"""

import urllib.request, urllib.parse, urllib.error
import json

apiKey = 42
serviceurl  = 'http://py4e-data.dr-chuck.net/json?'

link = input('Enter location: ')

parms = {'address': link , 'key': apiKey}   #according to dr chuck api key is 42

link = serviceurl  + urllib.parse.urlencode(parms)
print('Retrieving', link)

html = urllib.request.urlopen(link).read().decode()
print('Retrieved', len(html), 'characters')

try:
    data = json.loads(html)
except:
    raise Exception("Couldn't retreive Data")

placeId = data['results'][0]['place_id']
print('Place id', placeId)
