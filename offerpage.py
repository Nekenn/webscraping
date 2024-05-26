import csv
import json
from connexion import *
import re

from data.titleExtractor import TitleExtractor
from data.skuExtractor import SkuExtractor
from data.priceExtractor import PriceExtractor
from data.ratingExtractor import RatingAndReview
from data.availabilityExtractor import AvailabilityExtractor


json_data = []

with open('listingdata.csv', mode='r', newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    
    for row in csvreader:
        json_data.append(row)
i=0
for entry in json_data:
    url = entry.get('url',None)
    if url:
        scraping = Scraping(url)
        response=scraping.getReponse()
        if response.status_code==200:
            #upc, price, availability, title, reviews
            i+=1
            htmlstr = response.text
            listing=open('offerpage.html','w')
            listing.write(htmlstr)
            html = BeautifulSoup(htmlstr, 'lxml')

            title = TitleExtractor(html)
            print('-------------- ',i,' --------------')
            print('title: ',title.extractTitle())

            sku = SkuExtractor(html)
            print('sku: ', sku.extractData())

            price = PriceExtractor(html)
            print('price: ',price.extractData())

            ratingAndReview = RatingAndReview(html).extractData()
            print('rating and reviews: ',ratingAndReview)

            availability = AvailabilityExtractor(html).extractData()
            print('availability: ',availability)




           

           
            

    
    