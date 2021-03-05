# Libraries to Requests, BeautifulSoup, Pandas 
# PIP those in.
# sample ISBN 9780276440502
from bs4 import BeautifulSoup
import requests
import pandas as pd 
import numpy as np


#Build the URL
base ='https://www.abebooks.com/servlet/SearchResults?sts=t&cm_sp=SearchF-_-home-_-Results&ds=100&an=&tn=&kn=&isbn='
# Selectable 
ISBN =  input("Give us ISBN: ")
#ISBN = '9780276440502'
#  9780276440502 = Churchill  
# 9780394900810 = If I Ran the Zoo
URL = base + ISBN
page = requests.get(URL)

## Set up the beautiful soup parsing on that url
soup = BeautifulSoup(page.content, 'html.parser')

## Get all the results 
BookIs = soup.find('title')

## Get each li id into a list 
price = []
book_number = []
condition = []

for bk in soup.find_all(itemtype="http://schema.org/Book"):
    book_number.append(bk["id"])


## Gather Price into Lists 

for meta in soup.find_all("meta",  itemprop="price"):
    price.append(meta["content"])

# Gather ITEM condition = itemCondition

for meta in soup.find_all("meta",  itemprop="itemCondition"):
    condition.append(meta["content"])


## append the lists into a pandas dataframe we can work with later. 

book_data = pd.DataFrame(
     {'Number': book_number,
     'cost': price,
     'condition': condition
     })

book_data.cost = book_data.cost.astype(float)



bd_index = book_data.index
num_sellers = len(bd_index)

avg_price = book_data["cost"].mean()
avg_price = round(avg_price, 2)



#########
# # Debug
#print(book_data.shape)
# print(len(condition))
# print(len(price))
# print(len(book_number))
#print(book_data)
# types = book_data.dtypes
# print(types)
################################################
# Outputs  
##################################################################

print('########### Look up #########')
print('Searching for: ', ISBN, 'on')
print(URL)
print('Found')
print(BookIs.text)
print('########### The Book Details #########')

print("== There are: ", num_sellers, "sellers")
print("== The Average prices is:", avg_price)
print("== The Highest Price is:", book_data["cost"].max())
print("== The Lowest Price is:", book_data["cost"].min())
#print(book_data)
# da_count = book_data.count()
# print(da_count)
#print(len(cost), len(Condition), len(Number)) # Print all of them out here
