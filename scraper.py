#uses Requests and BeautifulSoup 
#PIP those in.
# sample ISBN 9780276440502
import requests
from bs4 import BeautifulSoup

#Build the URL
base ='https://www.abebooks.com/servlet/SearchResults?sts=t&cm_sp=SearchF-_-home-_-Results&ds=100&an=&tn=&kn=&isbn='
#ISBN =  input("Give us ISBN: ")
ISBN = '9780276440502'

URL = base + ISBN
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
type(soup)
## IDs we'll need
##id="topbar-search-result-count"

## Get all the results 
books = soup.find(id='main')

## Find price elements by HTML Class Name

price_elements = soup.find_all('div', class_= 'srp-item-price')
print(type(price_elements))
print(len(price_elements))
print(price_elements)

## Get a single price for book 1


# ## Output 
# print("Total books")
# print(num_books.prettify())