class RatingAndReview:
    def __init__(self, element):
        self.element = element
    
    def extractData(self):
        ratingValue = self.element.select_one('meta[itemprop$=ratingValue]')
        reviewCount = self.element.select_one('meta[itemprop$=reviewCount]')
        if ratingValue is None or reviewCount is None:
            return None
        return {"ratinValue":ratingValue['content'], "ratingCount":reviewCount['content']}