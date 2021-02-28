#uses Requests and BeautifulSoup 
#PIP those in.

import requests
from bs4 import BeautifulSoup

URL = 'https://www.abebooks.com/servlet/SearchResults?cm_sp=sort-_-SRP-_-Results&ds=100&kn=9780340837245&sortby=2'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

## IDs we'll need
##id="topbar-search-result-count"

## Results 
books = soup.find(id='main')

## Find Elements by HTML Class Name
# example job_elems = results.find_all('section', class_='card-content')
#<div class="srp-item-price" id="srp-item-price-2">US$ 1.03</div>
# for job_elem in job_elems:
#     print(job_elem, end='\n'*2)
price_elements = books.find_all('div', class_= 'srp-item-price')

for prices in price_elements:
    print(prices, end='\n'*2)

# ## Output 
# print("Total books")
# print(num_books.prettify())