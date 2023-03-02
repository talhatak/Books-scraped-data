#importing modules
import requests         
from bs4 import BeautifulSoup
import pandas as pd
import time

data = []   # empty list to store scraped data, then convert this list to dataframe.

for i in range(1,51):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"   #get link of of 50 pages one-by-one
    response = requests.get(url)        #fetch data
    soup = BeautifulSoup(response.text, "html5lib")     #soup object

    books = soup.find_all('article', class_='product_pod')


    for book in books:
        item = {}
        item['name'] = book.find('img', class_="thumbnail").attrs['alt']       #finding name of book
        item['price'] = book.find('p', class_="price_color").text[1:]          #finding price of book 
        item['Availability'] = book.find('p', class_="instock availability").text.replace('\n', '').strip()     #checking availability of book
        item['rating'] = book.find('p').attrs['class'][1]       #finding rating of book
        data.append(item)

df = pd.DataFrame(data)     #create dataframe
df.to_csv('books.csv')
df.to_excel('books.xlsx')

if __name__ == '__main__':
    while True:
        time_wait = 1/2     
        print('waiting')
        time.sleep(time_wait*60)    #program pause duration: 30secs