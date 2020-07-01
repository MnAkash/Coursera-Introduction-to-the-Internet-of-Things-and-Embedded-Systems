# -*- coding: utf-8 -*-
"""
Created on Fri May  8 00:43:43 2020

@author: akash
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
from tqdm import tqdm
import csv

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://www.medicaldirectorybd.com'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

specialist = dict()

tags = soup('a')  #Retrieve all of the the anchor tags

#All doctors' list page link retrieve
print('\rLink retrieving of specialists page...')
for tag in tqdm(tags):
    link = tag.get('href', None)
    content = tag.contents[0]
    if link[:51] == 'http://www.medicaldirectorybd.com/doctor/specialist' :
        #print('Doctor of:', content)
        #print(link)
        specialist[content] = link

#%%Link retrieving of each doctor
doctors_page_links = []

print('\rLink retrieving of each doctor...')

for content in tqdm(specialist):
    url = specialist[content]
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    tags = soup('a')
    for tag in tags:
        link = tag.get('href', None)
        if link[:51] == 'http://www.medicaldirectorybd.com/doctor/specialist' :
            if link not in doctors_page_links:
                doctors_page_links.append(link)
                #print(link)
#%%Data parsing and crating CSV file
                
header = ['Doctor\'s Name', 'Professional Degree' , 'Designation', 
           'Specialist On', 'Hospital Name', 'Chamber Name', 'Visiting Hour',
           'Chamber Location', 'Phone Number', 'Email Address']
dataPosition = [2,8,14,20,26,32,38,44,50,56]
data = []
print('\rData parsing and crating CSV file...')
with open('Doctors_List.csv', 'w', newline='', encoding="utf-8")as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for doctorURL in tqdm(doctors_page_links):
        url = doctorURL
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')     
        tag = soup.findAll('div', {'class':'main_tex'}) #it will find only one tag with this criteria

        for index in dataPosition:
            details = tag[0].contents[index] #tag[0] is the only element and here using 'contents' method of bs4 class
            data.append(details[details.find('nbsp')+4:])  #[7:] to cut out '  $nbsp'
        data[-1] = data[-1][:-14]  #stripping \t\t\t\t\t\t\r\n\t\t\t\t\t\t after mail address
        writer.writerow(data)
        data = []