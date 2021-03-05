#tutorials used:
# https://www.dataquest.io/blog/web-scraping-beautifulsoup/
# https://realpython.com/python-web-scraping-practical-introduction/


## Find Elements by HTML Class Name
# example job_elems = results.find_all('section', class_='card-content')
#<div class="srp-item-price" id="srp-item-price-2">US$ 1.03</div>
# for job_elem in job_elems:
#     print(job_elem, end='\n'*2)


## Find price elements by HTML Class Name
#book_elements = soup.find_all('li', class_= 'cf result-item')
## Get a single price for book 1
#single_book = book_elements[25]
#print(single_book)

# title = single_book.find("meta",  itemprop="author")
# print(title["content"])

#  <div class="srp-item-price" id="srp-item-price-1">US$ 1.00</div>
#  title = soup.find("meta",  property="og:title")


##########################################
#uses Requests and BeautifulSoup 
#PIP those in.
# sample ISBN 9780276440502
import requests
from bs4 import BeautifulSoup
import pandas as pd
import pandas as pd
lst1 = range(10)
lst2 = range(10)
lst3 = range(10)
percentile_list = pd.DataFrame(
    {'lst1Title': lst1,
     'lst2Title': lst2,
     'lst3Title': lst3
    })
print(percentile_list)

#Build the URL
base ='https://www.abebooks.com/servlet/SearchResults?sts=t&cm_sp=SearchF-_-home-_-Results&ds=100&an=&tn=&kn=&isbn='
#ISBN =  input("Give us ISBN: ")
ISBN = '9780276440502'

URL = base + ISBN
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
#type(soup)

tag = soup.find_all('span')
#type(tag)
print(tag.attrs)



## IDs we'll need
##id="topbar-search-result-count"

# ## Get all the results 
# books = soup.find(id='main')

# # for tag in soup.find_all('li'):
# #     print(f'{tag.name}: {tag.text}')

# price =[]
# for meta in soup.find_all("meta",  itemprop="price"):
#     price.append(meta["content"])

# print(price)
# print(len(price))