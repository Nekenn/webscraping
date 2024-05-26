from connexion import *
from bs4 import BeautifulSoup
import csv
scraping = Scraping("https://allo.ua/ua/rjukzaki-i-sumki/konstrukcija_rjukzaki_sumki-otdelenie_dlja_noutbuka/naznachenie_rjukzaki_sumki-gorodskoj/proizvoditel-xiaomi/")

response = scraping.getReponse()
print(response.status_code)
htmlstr = response.text
listing=open('listingpage.html','w')
listing.write(htmlstr)
html = BeautifulSoup(htmlstr, 'lxml')

elements = html.select(".product-card__content > a")

filename = 'listingdata.csv'
header =["url"]
for element in elements:
    print(element)
    print()
    with open(filename,'w',newline="") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(header)
        for element in elements:
            csvwriter.writerow([element['href']])
   
        
