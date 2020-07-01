# -*- coding: utf-8 -*-
"""
Created on Thu May  7 22:58:24 2020

@author: akash
"""

# week 4 Assignment 1

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#if a bad url found which certificate not in python official list, it gives error
# So we Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_486878.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#Retrieve all of the the anchor tags
sum = 0
tags = soup('span')
for tag in tags:
    sum += int(tag.contents[0])
print(sum)