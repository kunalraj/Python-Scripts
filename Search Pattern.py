# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 23:37:31 2018

@author: KUNAL RAJ BHARDWAJ
"""
f=open("D:\companies.txt", "r")
found = False
count=0
for line in f:
    if "Amazon" in line:
        found = True        
        count=count+1
if count > 0:
    print("Found")
    print(count)