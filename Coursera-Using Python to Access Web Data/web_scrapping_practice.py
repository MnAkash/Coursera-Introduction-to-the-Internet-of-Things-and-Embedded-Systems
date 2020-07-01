# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 01:14:04 2020

@author: akash
"""
#Email extract from text file
#s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
import re
lst =[]
f=open("C:\\Users\\akash\\Desktop\\web_scrapping\\data.txt", "r")
for line in f:
    data = re.findall('\S+@\S+', line)
    if len(data)!=0:      
        for d in data:
            lst.append(d)
        
print(lst)



#%% week 4
#There is library "urllib" to do all socket works to make it easy

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')
for line in fhand:
    print(line.decode().strip()) #strip() for stripping new line
    
#so we just get the webpage as a html file


#%%
#crawilling and scrapping web with regular expession is mesy
#there is "BeauitifulSoup" modiule to do that easily

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#if a bad url found thats certificate not in python official list, it gives error
# So we Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://www.medicaldirectorybd.com/doctor/specialist_doctor_detalis/3/458'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#Retrieve all of the the anchor tags

tags = soup('a')
for tag in tags:
    #print('TAG:', tag)
    print(tag['href']) #getting value of attibute  'href'
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)


#x = soup.findAll('div', {'class':'main_tex'})
