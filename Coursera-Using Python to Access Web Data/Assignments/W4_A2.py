# -*- coding: utf-8 -*-
"""
Created on Thu May  7 22:59:31 2020

@author: akash
"""

#week 4 Assignment 2
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = int(input('Enter Count: '))
position = int(input('Enter Position: '))
url = 'http://py4e-data.dr-chuck.net/known_by_Blake.html'
print('Retrieving: ',url)
while count:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the anchor tags
    tags = soup('a')                        #getting all anchor tag data
    url = tags[position-1].get('href',None) #retrieving links only from the position as per question asks
    print('Retrieving: ',url)
    count -= 1

x = url.find("_")
print('Last name: ',url[x+4:-5])

#%%
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