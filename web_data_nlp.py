#!/usr/bin/python3

import urllib.request
from bs4 import BeautifulSoup
website="http://php.net"

#data downloading
web_data=urllib.request.urlopen(website)

#printing data
#print (web_data.read())

#reading web data with html tags
clean_data=web_data.read()

#applying lib of html5 to scrap
get_clean=BeautifulSoup(clean_data, 'html5lib')

#getting only text formt data
final_data=get_clean.get_text()

#removing un-necessary space
good_data=final_data.strip()

#print good-data
new_data=[]

for i in good_data:
    j=i.split()
    new_data.append(j)
    print(new_data)
