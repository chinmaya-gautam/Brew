#!/usr/bin/python

from bs4 import BeautifulSoup, Tag

file = open("sample.html", "r")
html = file.read()

soup = BeautifulSoup(html, 'html.parser')
soup.prettify()

description = soup.find('p', itemprop='description').contents
str = ""
for unit in description:
    if type(unit) is Tag:
        print unit.string
        str += unit.string
    else:
        print unit
        str += unit
print str

#print soup




