import csv
import json
from connexion import *
import re

json_data = []

with open('listingdata.csv', mode='r', newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    for row in csvreader:
        json_data.append(row)

for entry in json_data:
    url = entry.get('url',None)
    if url:
        scraping = Scraping(url)
        response=scraping.getReponse()
        if response.status_code==200:
            #upc, price, availability, title, reviews
            htmlstr = response.text
            listing=open('offerpage.html','w')
            listing.write(htmlstr)
            html = BeautifulSoup(htmlstr, 'lxml')

            upc_element = html.select_one("table th:contains('UPC') + td")
            upc = upc_element.text
           
            price = None
            for th in html.select("table th"):
                if "Price (incl. tax)" in th.text:
                    price_element = th.find_next_sibling("td")
                    if price_element:
                        price = price_element.text
                    break
            if price:
                price = re.search("(\d+.\d+)",price)
                print(price.group())
            

    
    