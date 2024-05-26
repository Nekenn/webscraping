import requests
from bs4 import BeautifulSoup
from lxml import html as xhtml
class Scraping:
    def __init__(self,url):
        self.url = url
    
    def getReponse(self):
        headers ={
            'Host':'allo.ua',
            'User-Agent':'Mozilla/5.0 (X11UbuntuLinux x86_64rv:126.0) Gecko/20100101 Firefox/126.0',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language':'en-US,en;q=0.5',
            'Accept-Encoding':'gzip, deflate, br, zstd',
            'Upgrade-Insecure-Requests':'1',
            'Sec-Fetch-Dest':'document',
            'Sec-Fetch-Mode':'navigate',
            'Sec-Fetch-Site':'none',
            'Sec-Fetch-User':'?1',
            'Connection':'keep-alive',
            #'Cookie':'store=default_ua; frontend=4680d460e2d142d1831c0e1348882f70; is_bot=0; detect_mobile_type=0; _gcl_au=1.1.617952688.1716713941; __exponea_etc__=e5b29777-5fe7-42ee-9377-af9dc06b72e6; frontend_hash=oWqS3Q4680d460e2d142d1831c0e1348882f70aKq3rv; private_content_version=3b7fd1d6db127ea416537719f4b17f5e; t_s_c_f_l=0%3A2%3Aeb223196672e6343%3AjH878lBHPhQM18%2BDSLf9BA%3D%3D; _ga_9BQQ97VH3P=GS1.1.1716748015.2.1.1716748019.56.0.0; _ga=GA1.2.984407725.1716713942; __utma=45757819.984407725.1716713942.1716713944.1716748023.2; __utmc=45757819; __utmz=45757819.1716713944.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22msxKEd1et11wypo6UPWf%22%7D; _gid=GA1.2.535329134.1716713945; _fbp=fb.1.1716713945734.1479137040; store=default_ua; protocol=https; city_id=4; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22unknown%22%7D; __cf_bm=4nBq7OJLYjQGIOGtKZSJ4ExFo6jOpegjam9u4xfx50s-1716748019-1.0.1.1-rTK5jutptgx4Boz5BPqMtEiOatN.NHO67gfd7Jw6BAZW7dFT72UFjAGKv_XGrZG1v7fVBZuPkTtnjGHHayePSg; __exponea_time2__=4.5990519523620605; __utmb=45757819.1.10.1716748023; __insp_wid=1964961402; __insp_slim=1716748024202; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly9hbGxvLnVhL3VhL2RldHNraXllLWtvbnN0cnVrdG9yeS9wcm9penZvZGl0ZWwteGlhb21pLw%3D%3D; __insp_targlpt=0JTQuNGC0Y%2FRh9GWINC60L7QvdGB0YLRgNGD0LrRgtC_0YDQuCBYaWFvbWkg0LrRg9C%2F0LjRgtC4INCyINCa0LjRlNCy0ZYsINCj0LrRgNCw0ZfQvdGWIHwgQUxMTzog0YbRltC90Lgg0LIg0LzQsNCz0LDQt9C40L3Rlg%3D%3D; __insp_norec_sess=true',
            'Priority':'u=1',
                }

        response = requests.get(url=self.url,headers=headers)
        return response
    

    
    