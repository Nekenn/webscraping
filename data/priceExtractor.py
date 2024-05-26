class PriceExtractor: 
    def __init__(self,element):
        self.element = element
    
    def extractData(self):
        price = self.element.select_one("meta[itemprop$=price]")
        if price is None:
            return None
        return price['content']