class SkuExtractor:
    def __init__(self,element):
        self.element = element
    
    def extractData(self):
        title=self.element.select_one("meta[itemprop$=sku]")
        if title is None:
            return title
        return title['content']
