#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 16:12:20 2018

@author: LennardSchwarz
"""
#data can be interpreted the following way
#https://coinmetrics.io/on-data-and-certainty/

import requests
import tarfile

url = 'https://coinmetrics.io/data/all.tar.gz'  #data URL
r = requests.get(url) #call URL

#save file as "crypto.tar.gz"
with open('Data/crypto.tar.gz', 'wb') as f:  
    f.write(r.content)

#extract .tar.gz and save to folder "crypto" in Data folder
tar = tarfile.open('Data/crypto.tar.gz') 
tar.extractall(path='Data/crypto')
tar.close() 