# Libraries to Requests, BeautifulSoup, Pandas 
# PIP those in.
# sample ISBN 9780276440502
from bs4 import BeautifulSoup
import requests
import pandas as pd 


#Build the URL
base ='https://www.abebooks.com/servlet/SearchResults?sts=t&cm_sp=SearchF-_-home-_-Results&ds=100&an=&tn=&kn=&isbn='
# Selectable ISBN =  input("Give us ISBN: ")
# Fixed ISBN for processing
ISBN = '9780276440502'

URL = base + ISBN
page = requests.get(URL)

## Set up the beautiful soup parsing on that url
soup = BeautifulSoup(page.content, 'html.parser')

## Get all the results 
books = soup.find(id='main')
results = soup.find('ul', class_= 'result-set')




## Get each li id into a list 

book_number = []
for bk in soup.find_all(class_="cf result-item"):
    book_number.append(bk["id"])

## Gather Price into Lists 
price = []
for meta in soup.find_all("meta",  itemprop="price"):
    price.append(meta["content"])

# Gather ITEM condition = itemCondition

Condition =[]
for meta in soup.find_all("meta",  itemprop="itemCondition"):
    Condition.append(meta["content"])


## append the lists into a pandas dataframe we can work with later. 

book_data = pd.DataFrame(
    {'Book Number': book_number,
    'Price': price,
    'Condition': Condition
    })
book_data.Price = book_data.Price.astype(float)
# types = book_data.dtypes
# print(types)


bd_index = book_data.index
num_sellers = len(bd_index)

avg_price = book_data["Price"].mean()
avg_price = round(avg_price, 2)

################################################
# Outputs  
##################################################################

print("There are: ", num_sellers, "sellers")
print("The average prices is:", avg_price)

print(book_data)
