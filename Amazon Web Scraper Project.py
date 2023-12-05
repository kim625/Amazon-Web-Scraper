#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import smtplib #for sending email to myself
import datetime


# In[5]:


URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&custo'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36","Accept-Encoding": "gzip, deflate, br", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Upgrade-Insecure-Requests": "1"}

page = requests.get(URL,headers=headers) #bringing in the data from the URL

soup1 = BeautifulSoup(page.content, 'html.parser') #pulling every html on the website

soup2 = BeautifulSoup(soup1.prettify(), 'html.parser') #this will make the soup1 html format looks more cleaner.

title = soup2.find(id='productTitle').get_text().strip()

tag = soup2.find('span',class_='a-offscreen')
for i in tag:
    price=i.text

    
    
print(title)
print(price)


# In[3]:


price = price.strip()[1:] #cleared white space and removed a dollar sign
title = title.strip()

print(title)
print(price)


# In[6]:


import datetime

today = datetime.date.today()
print(today)


# In[10]:


import csv

header = ['Title', 'Price','Date']
data = [title, price, today] #put both of them into a list

#with open('Amazon Web Scraper.csv', 'w', newline='', encoding = 'UTF8') as f:
#    writer = csv.writer(f)
#    writer.writerow(header)
#    writer.writerow(data)


# In[34]:


import pandas as pd

df = pd.read_csv(r'C:\Users\Seohyun Kim\Amazon Web Scraper.csv')

print(df)


# In[9]:


#Now we are appending data to the csv

with open('Amazon Web Scraper.csv', 'a+', newline='', encoding = 'UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[8]:


def check_price():
    URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&custo'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36","Accept-Encoding": "gzip, deflate, br", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Upgrade-Insecure-Requests": "1"}

    page = requests.get(URL,headers=headers) #bringing in the data from the URL

    soup1 = BeautifulSoup(page.content, 'html.parser') #pulling every html on the website

    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser') #this will make the soup1 html format looks more cleaner.

    title = soup2.find(id="productTitle").get_text()

    tag = soup2.find('span',class_='a-offscreen')
    for i in tag:
        price=i.text
            
    price = price.strip()[1:] 
    
    title = title.strip()
    
    import datetime

    today = datetime.date.today()
    
    import csv

    header = ['Title', 'Price','Date']
    data = [title, price, today]
    
    with open('Amazon Web Scraper.csv', 'a+', newline='', encoding = 'UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        
    if price < 200:
        


# In[1]:


# Runs check_price after a set time and inputs data into your CSV

while(True):
    check_price()
    time.sleep(86400) #Check the price every 24 hours


# In[ ]:




