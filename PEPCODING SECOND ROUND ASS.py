#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests
 
# get URL
page = requests.get("https://en.wikipedia.org/wiki/V")
 
# scrape webpage
soup = BeautifulSoup(page.content, 'html.parser')
 
list(soup.children)
 
# find all occurrence of p in HTML
# includes HTML tags
#print(soup.find_all('p'))
 
 
# return only text
# does not include HTML tags
print(soup.find_all('h2')[1].get_text())
print(soup.find_all('p')[1].get_text(),end='')
print(soup.find_all('p')[2].get_text())
print(soup.find_all('p')[3].get_text())
print(soup.find_all('p')[4].get_text())

print(soup.find_all('h2')[2].get_text())
print(soup.find_all('p')[5].get_text())
print(soup.find_all('p')[6].get_text())
print(soup.find_all('li')[26].get_text())
print(soup.find_all('li')[27].get_text())
print(soup.find_all('li')[28].get_text())
print(soup.find_all('p')[7].get_text(),end='')
print(soup.find_all('p')[8].get_text())
print(soup.find_all('h2')[3].get_text())
print(soup.find_all('li')[29].get_text())
print(soup.find_all('li')[30].get_text())
print(soup.find_all('li')[31].get_text())
print(soup.find_all('li')[32].get_text())
print(soup.find_all('li')[33].get_text())
print(soup.find_all('li')[34].get_text())
print(soup.find_all('li')[35].get_text())
print(soup.find_all('li')[36].get_text())
print(soup.find_all('li')[37].get_text())
print(soup.find_all('p')[9].get_text())


# In[ ]:




