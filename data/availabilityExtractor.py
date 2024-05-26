class AvailabilityExtractor:
    def __init__(self,element):
        self.element = element

    def extractData(self):
        availability = self.element.select_one('link[itemprop$=availability]')
        return None if availability is None else availability['content']