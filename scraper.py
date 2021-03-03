#uses Requests and BeautifulSoup 
#PIP those in.
# sample ISBN 9780276440502
import requests
from bs4 import BeautifulSoup
# import pandas as pd 
import pandas as pd 


#Build the URL
base ='https://www.abebooks.com/servlet/SearchResults?sts=t&cm_sp=SearchF-_-home-_-Results&ds=100&an=&tn=&kn=&isbn='
#ISBN =  input("Give us ISBN: ")
ISBN = '9780276440502'

URL = base + ISBN
page = requests.get(URL)

## Set up the beautiful soup parsing on that url
soup = BeautifulSoup(page.content, 'html.parser')
type(soup)
## IDs we'll need
##id="topbar-search-result-count"

## Get all the results 
books = soup.find(id='main')
results = soup.find('ul', class_= 'result-set')
## Find price elements by HTML Class Name
#book_elements = soup.find_all('li', class_= 'cf result-item')
## Get a single price for book 1
#single_book = book_elements[25]
#print(single_book)

# title = single_book.find("meta",  itemprop="author")
# print(title["content"])

## Get each li id into a list 

book_number = []

for bk in results.find_all(class_="cf result-item"):
    book_number.append(bk["id"])

## Gather Price into Lists 
price =[]
for meta in results.find_all("meta",  itemprop="price"):
    price.append(meta["content"])

# Gather ITEM condition = itemCondition
Condition =[]
for meta in results.find_all("meta",  itemprop="itemCondition"):
    Condition.append(meta["content"])


## append the lists into a pandas dataframe we can work with later. 




################################################
# Outputs  
##################################################################
print("==================Print the Price array and Lengh ========")
print(book_number)
print("The lengh of price array:" + str(len(book_number)))
print("==================Print the Condition array and Lengh ========")


print("==================Print the Price array and Lengh ========")
print(price)
print("The lengh of price array:" + str(len(price)))
print("==================Print the Condition array and Lengh ========")

print(Condition)
print("The lengh of condition array:" + str(len(Condition)))
# print(type(book_elements))
# print(len(book_elements))

