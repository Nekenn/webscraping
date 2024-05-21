from connexion import *
from bs4 import BeautifulSoup
import csv
scraping = Scraping("http://books.toscrape.com/")

response = scraping.getReponse()

htmlstr = response.text
listing=open('listingpage.html','w')
listing.write(htmlstr)
html = BeautifulSoup(htmlstr, 'lxml')

elements = html.select(".image_container a")
filename = 'listingdata.csv'
header =["url"]
for element in elements:
    with open(filename,'w',newline="") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(header)
        for element in elements:
            csvwriter.writerow(["http://books.toscrape.com/"+element['href']])
        
