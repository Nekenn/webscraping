class TitleExtractor:
    def __init__(self,element):
        self.element = element
    
    def extractTitle(self):
        title=self.element.select_one(".p-view__header-title")
        if title is None:
            return title
        return title.text