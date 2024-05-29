from connexion import *
from bs4 import BeautifulSoup
import csv
scraping = Scraping("https://allo.ua/ua/zaschitnye-plenki-k-planshetam/")

response = scraping.getReponse()
print(response.status_code)
htmlstr = response.text

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
   
        
