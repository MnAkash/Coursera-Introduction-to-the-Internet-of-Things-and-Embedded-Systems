# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 01:02:54 2020

@author: akash
"""

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

link = "http://py4e-data.dr-chuck.net/comments_486880.xml"
html = urllib.request.urlopen(link).read().decode()
print('Retrieving', link)
print('Retrieved', len(html), 'characters')

#data calculation
count = 0
sum = 0
data = ET.fromstring(html)
tags = data.findall('comments/comment')

for tag in tags:
    count += 1
    sum += int(tag.find('count').text)
    
    
print('Count:', count)
print('Sum:', sum)