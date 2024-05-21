import requests
from bs4 import BeautifulSoup
from lxml import html as xhtml
class Scraping:
    def __init__(self,url):
        self.url = url
    
    def getReponse(self):
        response = requests.get(url=self.url)
        assert response.status_code == 200
        return response
    

    
    