# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:17:32 2020

@author: akash
"""

#week3 Request / Response Cycle
#Exploring the HyperText Transport Protocol

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #define socket connection
mysock.connect(('data.pr4e.org', 80))  #connect to port 80 (which is for web request)
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() #encode() converts unicode to utf-8
mysock.send(cmd)   # sending request
while True:
    data = mysock.recv(512)  #receive data from server upto 512 character
    if (len(data) < 1):    #while not data receiving
        break
    print(data.decode())    #decode byte data to utf-8 by default
mysock.close()

